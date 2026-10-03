# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

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

- [ ] Describe the game's purpose - A game designed to randomized integers which users can guess withing a given amount of attempts based on dificulty
- [ ] Detail which bugs you found. - 3 main bugs were the difficulty bug, the hint bug and the new game bug. The difficulty bug was incorrect for logically for what they claimed to be, the hint bug showed the wrong hint which was essentially backwards for the value entered, and the new game bug did not launch a new instance after the previous one was completed.
- [ ] Explain what fixes you applied. - Utilizing claude, the hint bug was easy to fix by just reversing the implemented logic. The difficulty bug was subsequently easy to fix by updateding the values for each level. The new game bug was more in depth as it required changing the logic behing the new game, for example, The secret was always drawn from 1–100, whatever the difficulty. On Easy (1–20) the secret could be 73, so the game was unwinnable. On Hard (1–200) it could never be above 100. After a win or loss, status stays "won" or "lost". The check at line 81 then stops the app, so New Game never lets you play again. A new status was added to remedy this. the value of score and history carried to the next game so we updated that to reset with each new game.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Select Difficulty in the left sidebar, eg. Hard
2. Enter a guess, eg. 2
3. Game returns too low, updates attempts
4. Enter 70
5. Returns too low
6. Enter 100
7. Returns too High
8. Enter 87
9. Returns You Won, show what the secret is and displays final score.
10. Click New game to begin again.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
tests\test_game_logic.py .........................                                                                                                                                                                        [100%]

====================================================================================================== 25 passed in 0.08s ======================================================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
