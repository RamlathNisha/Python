def main():
    grades = []
    while True:
        grade = input("Enter a grade (or 'q' to quit): ")
        if grade.lower() == 'q':
            break
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if len(grades) > 0:
        average_grade = sum(grades) / len(grades)
        print(f"Average grade: {average_grade}")
    else:
        print("No grades entered.")

if __name__ == "__main__":
    main()
