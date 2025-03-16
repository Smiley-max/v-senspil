import sys
import time
import random

def secure_shutdown():
    print("\n🚨 CRITICAL SECURITY BREACH DETECTED! SYSTEM IS SAFELY SHUTTING DOWN... 🚨")
    time.sleep(2)  # Simulate a slow shutdown
    sys.exit(0)  # Safely exits the program

def are_you_human():
    score = 0

    print("🛡️ SECURITY QUIZ: Are You a Human? 🛡️")
    print("⚠️ Warning: Incorrect answers may result in an immediate security shutdown!")

    start_time = time.time()  # Start timer

    # Question 1 - Simple math with a twist
    answer = input("1. What is 7 + 5? ").strip()
    if answer == "12":
        score += 1
    elif answer.lower() in ["robot", "i don't know"]:
        secure_shutdown()

    # Question 2 - Time-limited task
    print("\n2. Type the word 'human' exactly as shown, within 3 seconds!")
    time.sleep(0.5)  # Small delay for added stress
    answer = input("Type here: ").strip()
    if answer == "human" and (time.time() - start_time) < 3:
        score += 1
    else:
        secure_shutdown()

    # Question 3 - Human behavior (trick question)
    answer = input("\n3. If someone gives you a gift, what do you do?\n"
                   "a) Say 'thank you' and smile\n"
                   "b) Analyze if it's dangerous\n"
                   "c) Beep boop, I do not understand\n"
                   "Type a, b, or c: ").strip().lower()
    if answer == "a":
        score += 1
    elif answer in ["b", "c"]:
        secure_shutdown()

    # Question 4 - Trap
    answer = input("\n4. Are you a robot? (yes/no): ").strip().lower()
    if answer == "no":
        score += 1
    elif answer == "yes":
        secure_shutdown()

    # Question 5 - Randomized question to prevent predictability
    random_questions = [
        ("What color is a typical banana?", "yellow"),
        ("What do cows drink?", "water"),
        ("How many legs does a spider have?", "8"),
    ]
    question, correct_answer = random.choice(random_questions)
    answer = input(f"\n5. {question} ").strip().lower()
    if answer == correct_answer:
        score += 1
    else:
        secure_shutdown()

    print("\n📊 Security evaluation complete...")

    if score == 5:
        print("✅ You are a verified human! Welcome. 🏆")
    elif score >= 3:
        print("⚠️ You are probably human... but we are watching you. 🤨")
    else:
        secure_shutdown()  # Extra security if score is too low

# Run the quiz
are_you_human()