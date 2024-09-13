questions = [
    ["Who developed Python?", "Guido van Rossum", "Elon Musk", "Mark Zuckerberg", "Bill Gates", 1],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["Which element has the chemical symbol 'O'?", "Oxygen", "Hydrogen", "Gold", "Silver", 1],
    ["What is the largest ocean?", "Atlantic", "Indian", "Arctic", "Pacific", 4],
    ["Which country hosted the 2020 Olympics?", "USA", "Japan", "Brazil", "China", 2],
]

wallet = 0
levels = [10, 20, 30, 40, 50, 100]
level1 = 30
level2 = 50
level3 = 100

print("Welcome to Kon Banega Crorepati!")
for i in range(len(questions)):
    question = questions[i]

    print(f"Question for {levels[i]} Rs:\n{question[0]}")
    print(f"1. {question[1]}\n2. {question[2]}\n3. {question[3]}\n4. {question[4]}")
    try:
        ans = int(input("Enter your answer (1-4): "))
    except Exception as e:
        print("Invalid input! Please enter a number between 1 and 4.")
        break

    if ans == question[-1]:
        print(f"Correct! You have won {levels[i]} Rs.\n")
        wallet += levels[i]
    else:
        print(f"Wrong answer! You have lost. The correct answer was option {question[-1]}.\n")
        print(f"Thank you for playing!")
        break

    # Check if the player has reached a new level
    if wallet >= level3:
        print(f"Congratulations! You have reached level 3 and earned {level3} Rs.")
        break
    elif wallet >= level2:
        print(f"Congratulations! You have reached level 2 and earned {level2} Rs.")
    elif wallet >= level1:
        print(f"Congratulations! You have reached level 1 and earned {level1} Rs.")

# Final message
if wallet < level1:
    print(f"Thank you for playing! You have not crossed level 1.")
