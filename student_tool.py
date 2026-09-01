def main():
    student_name = input("Enter the student's name: ").strip()

    grades = []

    for assignment_number in range(1, 4):
        while True:
            try:
                grade = float(input(f"Enter grade for assignment {assignment_number}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")

    average = sum(grades) / len(grades)

    if average >= 90:
        status = "Excellent!"
    elif average >= 80:
        status = "Very Good!"
    elif average >= 70:
        status = "Good!"
    else:
        status = "Needs Improvement."

    print("\nStudent Grade Summary")
    print("-" * 30)
    print(f"Student Name: {student_name}")
    print(f"Assignment 1: {grades[0]:.1f}")
    print(f"Assignment 2: {grades[1]:.1f}")
    print(f"Assignment 3: {grades[2]:.1f}")
    print(f"Average Grade: {average:.2f}")

    print(f"Status: {status}")

if __name__ == "__main__":
    main()


#AI development notes

# One prompt I gave Copilot:
# Create a Python program for a student's name and three grades.

# One useful suggestion Copilot gave me:
# Copilot suggested checking that grades are between 0 and 100.
#
# One thing I changed or rejected:
# I added a status message.
#
# Why I made that decision:
# The assignment requires a status message.
#
# How I tested the finished program:
# I ran the program and tested it with three grades.