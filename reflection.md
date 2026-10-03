# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The infomation display on the screen did not match what was shown on the settings sidebar

- List at least two concrete bugs you noticed at the start  
  Difficulty was displayed incorrectly
  No indication/notification that a new game was started
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                         | Expected Behavior                    | Actual Behavior                                                   | Console Output / Error   | Suspected Code Location |
|-------------------------------|--------------------------------------|-------------------------------------------------------------------|--------------------------|-------------------------|
| Guess of 5                    | Hint Go Higher                       | Go Lower                                                          |                          | app.py, check_guess     |
| New Game after loss/Win       | Clear hint and Game restart          | Win/Loss messsage persists and no new hint is displayed           |                          | app.py Line 134         |
| Difficulty Hard               | Range 1 - 50, attempts allowed 5     | games displays Guess a number between 1 and 100. Attempts left: 4 |                          | app.py st.info Line 109 |
| Difficulty Settings           | Normal: 1-50                         | Normal: 1-100,                                                    |                          | get_range_for_difficulty|
| Difficulty Settings           | Hard: 1-100,                         | Hard: 1-50,                                                       |                          | get_range_for_difficulty|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  Claude sugessted the following - Hard was easier than Normal. Hard's range was 1–50 and Normal's was 1–100. I'd change Hard to 1–200.
  Hard difficulty having a larger guess range is logically sound since the attempts will be lower which increases the likelyhood of the user making a wrong guess.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  Cluade modified the update_score functions as such 
    points = 100 - 10 * (attempt_number)
  I disagreed with this since the maximum point a user will score will be 90 even if they guessed correctly on the first try, this also means that the score stayed the same regardless of dificulty so this was further changed to add bonuses for dificulty. We can improve on this to penalize users more as the dificulty increase.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  Running a manual test along with the pytest and actually playtesting the game to confirm bug was fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  The Win condition test showed a mismatch in type [returns a tuple like ('Win', '🎉 Correct!'). The tests test_winning_guess, test_guess_too_high and test_guess_too_low expect only the outcome string, such as "Win"], Cluade made some unilateral changes that could have gone unnoticed if not for the test failing.

- Did AI help you design or understand any tests? How?
  Having cluade spell out its changes made understaing the steps it took in testing the codes easier to.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit reruns typically do not prserve the state of the file since it runs the whole python file from top to bottom, but using the session.state disctionary, we can accomplish this. The state here mean that we dont wipe data every time we rerun.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I initially allowed claude to make changes to the whole file in logic_utils which made review the code problematic so learning to take time and make changes in small pieces was very beneficial
- What is one thing you would do differently next time you work with AI on a coding task?
  I would prefer to work on the bugs individually and rely on the AI to assist with concept i may be struglling with rather than have the AI write/fix things.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I see it as a tool that can let a developer think out their ideas and plan when they hit a wall. rather than having the AI write the code (which can be bug ridden), the develpoer can bounce their thoughts to the AI to come to a conclusion.