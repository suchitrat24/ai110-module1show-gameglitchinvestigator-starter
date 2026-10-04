# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

 The game first had wrong results printing out for my answers. The first bug was that the hints were backwards: if my guess was too high, the game told me to "Go HIGHER!", and if it was too low, it said "Go LOWER!". The second bug was that on every other attempt the game turned the secret number into a string, so it compared my guess as text instead of as a number. That made the hints wrong in a different way, because "9" counts as bigger than "50" when you compare text. A third bug was that the "New Game" button didn't fully reset the game, so after winning or losing I was still stuck on the "Game over" / "You already won" message.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret is 50, guess 60 | "Too High" with a hint to go lower | "Too High" but the hint says "📈 Go HIGHER!" | None (logic bug, no error) |
| Secret is 50, guess 9 on the 2nd (even) attempt | "Too Low" | "Too High", because "9" > "50" when compared as text | None (the TypeError was caught silently by a `try/except`) |
| Win or lose a game, then click "New Game 🔁" | A fresh game starts | Still shows "You already won" / "Game over" because `status` is never reset | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used Claude Code inside VS Code. I asked it to find three bugs in `app.py`, then had it fix the first two, mark each spot with a `# FIXME` comment, and move `check_guess` into `logic_utils.py`. One correct suggestion was that the hint messages in `check_guess` were swapped. I had to reject how Claude wanted to test the game and I had to ask it to write it as a separate file. I verified that by having it write a pytest case (`test_hint_direction_not_swapped`) that checks a guess of 60 against a secret of 50 says "LOWER" and a guess of 40 says "HIGHER", and the test passed. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I counted a bug as fixed when a test that targets that exact behavior passed. The first time I ran pytest, it wasn't even installed in my virtual environment, so I had to install it from `requirements.txt`. After that, my new hint test passed, but the three starter tests failed. They compared the result to a plain string like `"Win"`, while `check_guess` actually returns a pair like `("Win", "🎉 Correct!")`. I updated them to unpack the outcome first, and then all 4 tests passed. The AI helped me design the hint test: it pointed out that checking only "Too High" / "Too Low" wouldn't catch the bug, because those labels were already right and only the messages were swapped.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time you click a button or type something, Streamlit runs your whole Python script again from top to bottom. That means normal variables get reset on every click, so if the secret number were a regular variable, it would change every time you guessed. `st.session_state` is like a notebook that survives those reruns, so the secret, attempts, score, and history stay the same between clicks. The "New Game" bug comes from this too: the button only reset some of the values in session state and forgot `status`, so the old "game over" state carried over into the new game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is marking the "crime scene" with a `# FIXME` comment and then writing a test that targets that exact bug, so I can prove the fix worked instead of just trusting it. Next time, I would run the program and reproduce each bug myself before asking the AI to fix it, so I'm not relying only on its explanation. I think AI is a very convienent way to code faster but the higher you give AI with specific prompts the better you are able to finish your work. 
