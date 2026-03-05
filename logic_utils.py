# logic_utils.py

def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    elif difficulty == "Normal":
        return 1, 50
    else:
        return 1, 100

def parse_guess(raw: str):
    if not raw:
        return False, None, "Enter a guess."
    try:
        value = int(float(raw))
        return True, value, None
    except ValueError:
        return False, None, "That is not a number."

def check_guess(guess, secret):
    guess = int(guess)
    secret = int(secret)
    if guess == secret:
        return "Win"
    elif guess > secret:
        return "Too High"
    else:
        return "Too Low"

def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = max(10, 100 - 10 * attempt_number)
        return current_score + points
    return current_score # Simplified for now