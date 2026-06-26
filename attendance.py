from utils import calculate_percentage, risk_level, classes_needed

class Subject:
    def __init__(self, name, attended, total):
        self.name = name
        self.attended = attended
        self.total = total

    def get_report(self):
        percent = calculate_percentage(self.attended, self.total)
        risk = risk_level(percent)
        needed = classes_needed(self.attended, self.total)

        return {
            "name": self.name,
            "percent": round(percent, 2),
            "status": risk,
            "needed": needed
        }