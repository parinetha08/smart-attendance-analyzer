def calculate_percentage(attended, total):
    if total == 0:
        return 0
    return (attended / total) * 100


def risk_level(percentage):
    if percentage >= 75:
        return "SAFE"
    elif percentage >= 65:
        return "WARNING"
    else:
        return "DANGER"


def classes_needed(attended, total):
    required = 0.75 * total
    if attended >= required:
        return 0
    return int(required - attended + 1)