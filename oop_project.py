class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        """Calculates the average score of the student."""
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def is_passing(self, passing_score=40):
        """Checks if the student is passing all subjects."""
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        """Adds a student and their scores to the tracker."""
        student = Student(name, scores)
        self.students[name] = student

    def calculate_class_average(self):
        """Calculates the overall average score for the class."""
        if not self.students:
            return 0
        total_scores = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students)

    def display_student_performance(self):
        """Displays each student's performance, including average score and pass/fail status."""
        for name, student in self.students.items():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"{name}: Average = {average:.2f}, Status = {status}")
        class_avg = self.calculate_class_average()
        print(f"\nClass Average: {class_avg:.2f}")


def get_student_scores():
    """Prompts the teacher for a student's scores in three subjects and validates input."""
    scores = []
    subjects = ["Math", "Science", "English"]
    for subject in subjects:
        while True:
            try:
                score = int(input(f"Enter the score for {subject}: "))
                if 0 <= score <= 100:  # Assuming scores are out of 100
                    scores.append(score)
                    break
                else:
                    print("Please enter a score between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return scores


def main():
    tracker = PerformanceTracker()
    while True:
        name = input("Enter student's name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        scores = get_student_scores()
        tracker.add_student(name, scores)

    print("\n--- Student Performance Summary ---")
    tracker.display_student_performance()


if __name__ == "__main__":
    main()

