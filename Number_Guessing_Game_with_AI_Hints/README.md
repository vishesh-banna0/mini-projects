# 🎯 Number Guessing Game with AI Hints

A fun **Number Guessing Game** where the AI picks a random number between **1 and 100**, and the player must guess it. The game provides smart hints to guide the player based on their guess.

## 🚀 How It Works:
1. The AI picks a **random number** between **1 and 100**.
2. The player makes guesses, and the game provides hints:
   - **"Too high! Go lower."** if the guess is too high.
   - **"Too low! Go higher."** if the guess is too low.
   - **"You are very close! Go slightly up/down."** if the guess is within **3 numbers** of the correct answer.
3. The game continues until the player **guesses the correct number**.

## 🔧 Functions Used:
- `random.randint(1, 100)`: Selects a random number between **1 and 100**.
- `range(start, end)`: Used to check if the guess is close to the correct number.
- `input()`: Takes user input for guessing.

## 💡 Approach:
1. **AI chooses a random number** between **1 and 100**.
2. The user **enters a guess**.
3. The game checks:
   - If the number is **out of bounds**, a warning is displayed.
   - If the guess is **correct**, the game announces the win.
   - If the guess is **close** (within 3 numbers), it provides a *"very close"* hint.
   - Otherwise, it gives a **higher/lower** hint.
4. The game **loops until the correct guess is made**.

## 🎮 Example Gameplay:
```
Game is ON
I have chosen a number between 1 and 100.
Your task is to guess the number correctly.

Enter Your Guess: 50
📈 Too low! Go higher.

Enter Your Guess: 75
📉 Too high! Go lower.

Enter Your Guess: 73
🔥 You are very close! Go slightly down.

Enter Your Guess: 72
🎉 Bingo!! That's the number!
```

## 🏆 Why This Project?
- Strengthens **Python basics** (loops, conditions, user input).
- Introduces **random number generation**.
- Enhances **logical thinking** with AI-driven hints.

---
Happy Guessing! 🔥🎲

