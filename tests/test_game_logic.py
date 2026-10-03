import pytest
from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_hint_direction_matches_outcome():
    # Regression: hints were swapped ("Too High" told the player to go higher)
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")

def test_numeric_comparison_not_string_comparison():
    # Regression: the secret was cast to str on even attempts, so 9 vs 10
    # was compared as "9" > "10" (True) instead of 9 < 10.
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"
    outcome, _ = check_guess(100, 20)
    assert outcome == "Too High"

def test_string_secret_is_not_supported_silently():
    # The str fallback was removed; a str secret must not give a bogus hint.
    import pytest
    with pytest.raises(TypeError):
        check_guess(9, "10")


def test_update_score_win_first_attempt_scores_100():
    assert update_score(0, "Win", 1) == 100


def test_update_score_win_points_decrease_per_attempt():
    assert update_score(0, "Win", 3) == 80
    assert update_score(50, "Win", 2) == 140


def test_update_score_win_has_minimum_of_10_points():
    assert update_score(0, "Win", 11) == 10
    assert update_score(0, "Win", 20) == 10


def test_update_score_difficulty_bonus_increases_with_difficulty():
    easy = update_score(0, "Win", 1, "Easy")
    normal = update_score(0, "Win", 1, "Normal")
    hard = update_score(0, "Win", 1, "Hard")
    assert easy < normal < hard
    assert (easy, normal, hard) == (100, 150, 200)


def test_update_score_bonus_applies_on_later_attempts():
    assert update_score(0, "Win", 3, "Hard") == 80 + 100


@pytest.mark.parametrize("difficulty", ["Easy", "Normal", "Hard"])
def test_update_score_first_try_is_max_for_difficulty(difficulty):
    first = update_score(0, "Win", 1, difficulty)
    assert all(update_score(0, "Win", n, difficulty) < first for n in range(2, 15))


def test_update_score_unknown_difficulty_gives_no_bonus():
    assert update_score(0, "Win", 1, "Impossible") == 100


def test_update_score_bonus_not_applied_on_wrong_guess():
    assert update_score(20, "Too High", 1, "Hard") == 15


@pytest.mark.parametrize("attempt", [1, 2, 3, 4])
def test_update_score_too_high_always_penalizes(attempt):
    # Regression: "Too High" on even attempts used to award +5
    assert update_score(20, "Too High", attempt) == 15


@pytest.mark.parametrize("attempt", [1, 2, 3, 4])
def test_update_score_too_low_always_penalizes(attempt):
    assert update_score(20, "Too Low", attempt) == 15


def test_update_score_unknown_outcome_unchanged():
    assert update_score(42, "Something Else", 1) == 42
