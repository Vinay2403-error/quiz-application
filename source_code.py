import tkinter as tk
from tkinter import messagebox
import random

# -------------------------------
# Load Questions from Text File
# -------------------------------
questions = []

with open("questions.txt", "r") as file:
    for line in file:
        data = line.strip().split("|")

        questions.append({
            "question": data[0],
            "A": data[1],
            "B": data[2],
            "C": data[3],
            "D": data[4],
            "answer": data[5]
        })

# Randomize question order
random.shuffle(questions)

# -------------------------------
# Variables
# -------------------------------
current_question = 0
score = 0

# -------------------------------
# Functions
# -------------------------------

def load_question():
    global current_question

    if current_question >= len(questions):
        show_result()
        return

    q = questions[current_question]

    question_label.config(text=q["question"])

    btnA.config(text="A. " + q["A"])
    btnB.config(text="B. " + q["B"])
    btnC.config(text="C. " + q["C"])
    btnD.config(text="D. " + q["D"])

    progress_label.config(
        text=f"Question {current_question + 1} of {len(questions)}"
    )


def check_answer(choice):
    global current_question
    global score

    q = questions[current_question]

    if choice == q["answer"]:
        score += 1

    current_question += 1
    load_question()


def show_result():

    percentage = (score / len(questions)) * 100

    messagebox.showinfo(
        "Quiz Result",
        f"Quiz Completed!\n\n"
        f"Score: {score}/{len(questions)}\n"
        f"Percentage: {percentage:.2f}%"
    )

    root.destroy()


def quit_quiz():

    if messagebox.askyesno(
        "Quit Quiz",
        "Are you sure you want to quit?"
    ):
        attempted = current_question

        if attempted > 0:
            percentage = (score / attempted) * 100
        else:
            percentage = 0

        messagebox.showinfo(
            "Result",
            f"Questions Attempted: {attempted}\n"
            f"Correct Answers: {score}\n"
            f"Percentage: {percentage:.2f}%"
        )

        root.destroy()


# -------------------------------
# GUI Window
# -------------------------------

root = tk.Tk()

root.title("Quiz Application")
root.geometry("700x500")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="GENERAL KNOWLEDGE QUIZ",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=20)

progress_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)

progress_label.pack()

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    wraplength=600,
    justify="center"
)

question_label.pack(pady=30)

btnA = tk.Button(
    root,
    width=40,
    height=2,
    font=("Arial", 12),
    command=lambda: check_answer("A")
)

btnA.pack(pady=5)

btnB = tk.Button(
    root,
    width=40,
    height=2,
    font=("Arial", 12),
    command=lambda: check_answer("B")
)

btnB.pack(pady=5)

btnC = tk.Button(
    root,
    width=40,
    height=2,
    font=("Arial", 12),
    command=lambda: check_answer("C")
)

btnC.pack(pady=5)

btnD = tk.Button(
    root,
    width=40,
    height=2,
    font=("Arial", 12),
    command=lambda: check_answer("D")
)

btnD.pack(pady=5)

quit_button = tk.Button(
    root,
    text="Quit Quiz",
    bg="red",
    fg="white",
    width=20,
    font=("Arial", 12, "bold"),
    command=quit_quiz
)

quit_button.pack(pady=20)

# Load First Question
load_question()

# Run Application
root.mainloop()