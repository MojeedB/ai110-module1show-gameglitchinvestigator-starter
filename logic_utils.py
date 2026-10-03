#FIX: Refactored logic into logic_utils.py using agent mode, changed range for each level
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#FIX: Refactored logic into logic_utils.py using agent mode, swapped hint so it correctly displays 
# higher or lower depending on the input and secret. eg. secret is 5, input is 4, ouput should be go higher
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


DIFFICULTY_BONUS = {"Easy": 0, "Normal": 50, "Hard": 100}

#FIX: Refactored logic into logic_utils.py using agent mode, modified the score to fix errornuoes scores base
#       on even odd numbers, added difficulty bonuses, and allowed for maximum score.
def update_score(current_score: int, outcome: str, attempt_number: int, difficulty: str = "Easy"):
    """
    Update score based on outcome, attempt number (1-based) and difficulty.

    A win scores 100 points on the first attempt, losing 10 per extra attempt
    (minimum 10), plus a difficulty bonus (harder = bigger bonus). A first-try
    win therefore always earns the maximum points for that difficulty.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points + DIFFICULTY_BONUS.get(difficulty, 0)

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
