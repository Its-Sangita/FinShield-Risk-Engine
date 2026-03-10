import csv
import os

class RiskEngine:
    def __init__(self, filename):
        self.filename = filename
        self.applicants = []

    def load_data(self):
        if not os.path.exists(self.filename):
            print(f"Error: {self.filename} not found.")
            return
        
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.applicants.append(row)

    def calculate_score(self, data):
        score = 0
        income = float(data['income'])
        expenses = float(data['expenses'])
        stability = float(data['years_in_business'])
        savings = float(data['savings'])

        # Logic 1: Debt-to-Income (40 pts)
        if (income - expenses) > (income * 0.5): score += 40
        elif (income - expenses) > (income * 0.2): score += 20

        # Logic 2: Stability (30 pts)
        if stability >= 3: score += 30
        elif stability >= 1: score += 15

        # Logic 3: Reserves (30 pts)
        if savings > (expenses * 6): score += 30
        elif savings > (expenses * 2): score += 15

        return score

    def run_assessment(self):
        print(f"{'Name':<15} | {'Score':<5} | {'Status'}")
        print("-" * 40)
        for person in self.applicants:
            score = self.calculate_score(person)
            status = "Approved" if score >= 70 else "Review" if score >= 40 else "Rejected"
            print(f"{person['name']:<15} | {score:<5} | {status}")

if __name__ == "__main__":
    engine = RiskEngine('applicants.csv')
    engine.load_data()
    engine.run_assessment()
