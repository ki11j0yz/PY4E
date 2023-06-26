#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

#use this table: [score: >=0.9, grade: A], [score: >= 0.8, grade: B], [score: >= 0.7, grade: C], [score: >= 0.6, grade: D], [score: < 0.6, grade: F]:

ques_total = input("Enter total questions: ")
ques_right = input("Enter total number correct: ")
score = float(ques_right) / float(ques_total)
score = (round(score, 2))
print(score)
if score >= 0.9:
    print("A")
if score <= 0.9:
    if score >= 0.8:
        print("B")
    elif score >= 0.7 and score <= 0.8:
        print("C")
    elif score >= 0.6 and score <= 0.7:
        print("D")
    elif score <= 0.6:
        print("F")