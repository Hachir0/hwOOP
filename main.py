class Student:
    def __init__(self, name, surname, gender, courses_in_progress):
        self._name = name
        self._surname = surname
        self._gender = gender
        self._finished_courses = []
        self._courses_in_progress = courses_in_progress
        self._grades = {}
    
    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer._courses_attached and course in self._courses_in_progress and 1 <= grade <= 10):
            
            if course not in lecturer._grades:
                lecturer._grades[course] = []
            lecturer._grades[course].append(grade)
        else:
            return 'Ошибка'
    
    def _get_average_grade(self):
        if not self._grades:
            return 0
        all_grades = [grade for grades in self._grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades)

    def compar(self, student2):
        if not isinstance(student2, Student):
            return "type dot't equal"
        if self._get_average_grade() - student2._get_average_grade() == 0:
            return f"The average scores equals, average score: {self._get_average_grade()}"
        
        elif self._get_average_grade() - student2._get_average_grade() < 0:
            return f"{student2._name}'s average score is higher, avarage score: {student2._get_average_grade()}"
        
        else:
            return f"{self._name}'s average score is higher, average score: {self._get_average_grade()}"
    
    def __str__(self):
        finished = ", ".join(self._finished_courses) if self._finished_courses else "None"
        in_progress = ", ".join(self._courses_in_progress) if self._courses_in_progress else "None"
        return (
            f"Name: {self._name}\n"
            f"Surname: {self._surname}\n"
            f"Finished courses: {finished}\n"
            f"Courses in progress: {in_progress}\n"
            f"Average rate for Homework: {self._get_average_grade():.1f}\n"
        )
            
            
class Mentor:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self._grades = {}
        self._courses_attached = courses_attached
        
    def _get_average_grade(self):
        if not self._grades:
            return 0
        all_grades = [grade for grades in self._grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades)
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()
    
    def __str__(self):
        return (
            f"Name: {self._name}\n"
            f"Surname: {self._surname}\n"
            f"Average rate: {self._get_average_grade():.1f}\n"
        )


class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self._courses_attached = courses_attached
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self._courses_attached and course in student._courses_in_progress:
            if course in student._grades:
                student._grades[course] += [grade]
            else:
                student._grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        courses = ", ".join(self._courses_attached) if self._courses_attached else "None"
        return (
            f"Name: {self._name}\n"
            f"Surname: {self._surname}\n"
            f"Courses attached: {courses}\n"
        )
     
        
stud = Student("Danil", "Mitrofan", "m", ["Python", "Java"])
stud2 = Student("Kamilla", "Garage", "w", ["Python", "Java"])

lecture = Lecturer("Oleg", "Polyakov", ["Python"])
lecture2 = Lecturer("Maria", "Golosova", ["Python", "GO"])

rev = Reviewer("Kama", "Aliev", ["Python", "JS"])
rev2 = Reviewer("Marat", "Alencov", ["Java", "pYTHON"])

rev.rate_hw(stud, "Python", 8)
rev2.rate_hw(stud, "Python", 10)

rev.rate_hw(stud2, "Python", 9)
rev2.rate_hw(stud2, "Python", 7)

stud.rate_lecturer(lecture, "Python", 10)
stud2.rate_lecturer(lecture, "Python", 8)

stud.rate_lecturer(lecture2, "Python", 7)
stud2.rate_lecturer(lecture2, "Python", 9)


print(stud)
print(lecture)
print(rev)


print(stud > stud2)
print(lecture.compar(lecture2))
