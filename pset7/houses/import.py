import csv
from sys import argv
import cs50

def importCSV():

    if len(argv) > 1:
        #create db file for easier testing
        open("students.db", "w").close()
        # open db file for SQLite
        db = cs50.SQL("sqlite:///students.db")
        # create student table in SQL db
        db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")

        # open CSV file
        with open(argv[1]) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            lines = 0
            for row in csv_reader:
                # read csv body
                if lines != 0:
                    names = row[0].split()
                    first = names[0]
                    middle = names[1] if len(names) == 3 else None
                    last = names[2] if len(names) == 3 else names[1]
                    house = row[1]
                    birth = row[2]

                    # insert data into db
                    db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", first, middle, last, house, birth)

                lines += 1

    else:
       print("Please enter a path to a CSV file.")
       return

importCSV()