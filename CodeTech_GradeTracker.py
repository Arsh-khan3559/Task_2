def get_grades():
    grades = {}
    print("Enter grades for each subject. Type 'done' when you are finished.")

    while True:
        subject = input("Enter the subject name (or 'done' to finish): ").strip()
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter the grade for {subject}: ").strip())
            if 0 <= grade <= 100:
                grades[subject] = grade
            else:
                print("Grade should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    
    return grades

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)

def determine_overall_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def display_results(grades, average, overall_grade):
    print("\n--- Grade Report ---")
    for subject, grade in grades.items():
        print(f"Subject: {subject}, Grade: {grade:.2f}")
    
    print(f"\nAverage Grade: {average:.2f}")
    print(f"Overall Grade: {overall_grade}")

def main():
    print("Welcome to the Student Grade Tracker!\n")
    grades = get_grades()
    
    if not grades:
        print("No grades were entered.")
        return
    
    average = calculate_average(grades)
    overall_grade = determine_overall_grade(average)
    
    display_results(grades, average, overall_grade)

if __name__ == "__main__":
    main()
