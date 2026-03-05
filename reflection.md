# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

Response: The hints were wrong and unhelpful. Even when I wrote the correct answer it wouldn't count it as correct. Though the UI worked the main concept of the game didn't.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Response: I used Google AI Studio: I implemented the check guess, as it switched them, so the hints work, I also made it so the submission works with the AI, so it actually submits properly and starts a new game. There was nothing wrong that the AI did, it pretty much got everything correct. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

Response: I used Pytest, Pytest allows me to see cleanly and nicely how my code ran! AI helped me make pytest files and recreate the logic_util.py file, so it actually works and all the tests work.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Response: Essentially everytime that I was clicking a button it rerean the script, so it'd generate a new secret, so I'd never get the "right" number/secret. If I had to explain it's be like playing hangman on a white board and everytime you guessed a vowel it'd rewrite to a new word.

- What change did you make that finally gave the game a stable secret number?

Response: I made it so the secret number was only generated if not already present in streamlit's memory with if "secret" not in st.session_state, that way it wouldn't regenerate it.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Response: I'd use pytest, I'd make sure to take more time to try and figure it out myself, the project has shown me that AI has come a long way, and is getting better and better at coding, which is great. I do believe it'll be best if people use their own minds to code. 
