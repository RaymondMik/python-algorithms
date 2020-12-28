from sys import argv
import cs50

def createRoster():

    if len(argv) > 1:
        # get house name
        house_name = argv[1]
        # open db file for SQLite
        db = cs50.SQL("sqlite:///students.db")
        # read db
        students = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last ASC, first", house_name)

        # print students
        for student in students:
            middle_name = " " + student['middle'] if student['middle'] else ""
            name = student['FIRST'] + middle_name + " " + student['LAST']
            print(f"{name}, born {student['birth']}")

        # print Not found
        if len(students) == 0:
            print(f"No students were found in {house_name}")
            return
    else:
       print("Please enter the name of a house.")
       return

createRoster()
