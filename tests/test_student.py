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

def test_add_class():
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
    new_class = "Art"
    
    student = Student(name, grade, classes)
    class_to_add = student.add_class(new_class)

    assert len(student.classes) == 6
    