from logic_utils import check_guess

# Collaboration: the AI noticed these starter tests compared against a plain
# string while check_guess returns (outcome, message); I approved unpacking it.

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_direction_not_swapped():
    # Bug: a guess above the secret said "Go HIGHER!" (and vice versa).
    # Collaboration: I asked the AI for a test targeting this bug; it checks
    # the message too, since the outcome labels were already correct.
    # A too-high guess should tell the player to go LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

    # A too-low guess should tell the player to go HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
