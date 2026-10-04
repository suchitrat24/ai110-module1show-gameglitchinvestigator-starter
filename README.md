# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

**Game Purpose:** A Streamlit number-guessing game. The player picks a difficulty (Easy 1–20, Normal 1–100, Hard 1–50), then tries to guess a secret number within a limited number of attempts. After each guess the game says whether it was too high or too low, and the player earns or loses points along the way.

**Bugs Found:**

1. **Backwards hints:** `check_guess` returned "📈 Go HIGHER!" when the guess was too high and "📉 Go LOWER!" when it was too low.
2. **Secret compared as text:** on every even attempt, `app.py` turned the secret into a string before checking the guess. Comparing an `int` to a `str` raised a `TypeError`, which a fallback caught and then compared the values as text, so "9" counted as bigger than "50".
3. **"New Game" doesn't reset:** the button never resets `status`, `score`, or `history`, so after a win or loss the game stays stuck on "You already won" / "Game over". It also ignores the difficulty's range and resets attempts to 0 instead of 1.

**Fixes Applied:**

- **Hints:** swapped the hint messages so a too-high guess says "Go LOWER!" and a too-low guess says "Go HIGHER!".
- **Secret type:** removed the even-attempt string conversion so guesses are always compared against the integer secret, and removed the text-comparison fallback in `check_guess`.
- **New Game:** the button now resets `status`, `score`, `history`, and attempts (back to 1, the same as a fresh page load), and picks the new secret from the current difficulty's range.
- **Refactor:** moved `check_guess` from `app.py` into `logic_utils.py`, and `app.py` now imports it.
- **Tests:** added `test_hint_direction_not_swapped`, which checks the hint message as well as the outcome label, and updated the starter tests to unpack the `(outcome, message)` pair that `check_guess` returns. All 4 tests pass.

## 📸 Demo Walkthrough

A sample game on **Normal** difficulty (range 1–100, 8 attempts), with "Show hint" checked. The "Developer Debug Info" panel shows the secret is **58** and the score starts at **0**.

1. User enters a guess of **40** and clicks "Submit Guess 🚀".
2. Game returns **"Too Low"** and shows the hint **"📈 Go HIGHER!"**. Score drops by 5 to **-5**.
3. User enters a guess of **70**, and the game returns **"Too High"** with the hint **"📉 Go LOWER!"**. Score drops by 5 to **-10**.
4. The secret stays at 58 between guesses, and the hints now point toward it. Before the fix, a too-high guess said "Go HIGHER!", and on even attempts guesses were compared as text.
5. User enters a guess of **58**. Balloons appear and the game shows **"You won! The secret was 58. Final score: 40"** (a win on this attempt is worth +50).
6. The game ends: submitting another guess shows "You already won. Start a new game to play again."
7. User clicks **"New Game 🔁"**. A new secret is picked from 1–100, the score and history reset, and the user can play again.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python -m pytest tests -v
============================= test session starts =============================
platform win32 -- Python 3.13.15, pytest-9.1.1, pluggy-1.6.0
rootdir: D:\CodePath AI 110\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collecting ... collected 4 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 25%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 50%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 75%]
tests/test_game_logic.py::test_hint_direction_not_swapped PASSED         [100%]
============================== 4 passed in 0.06s ==============================
```


