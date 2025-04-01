from school_schedule.student import Student

def test_student_class_instantiation():
    # arrange
    name = "Quinn" 
    grade = "junior"
    classes = [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
    # act
    student = Student(name, grade, classes)

    # assert
    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes