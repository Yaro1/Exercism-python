class School:
    def __init__(self):
        self.grades = dict()

    def add_student(self, name, grade):
        if grade in self.grades.keys():
            self.grades[grade].append(name)
        else:
            self.grades[grade] = [name]

    def roster(self):
        answer = []
        for i in [self.grade(x) for x in sorted(self.grades.keys())]:
            answer += i
        return answer

    def grade(self, grade_number):
        if grade_number in self.grades.keys():
            return sorted(self.grades[grade_number])
        else:
            return []