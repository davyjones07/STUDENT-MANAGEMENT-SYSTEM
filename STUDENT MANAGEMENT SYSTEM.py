import sqlite3

class Student:

        def insert_data(self,ROLL_NUMBER,NAME,AGE,GENDER,TOTAL_MARK,RANK):
                self.ROLL_NUMBER = ROLL_NUMBER
                self.NAME = NAME
                self.AGE = AGE
                self.GENDER = GENDER
                self.TOTAL_MARK = TOTAL_MARK
                self.RANK = RANK
                con = sqlite3.connect('studentDB.db')
                cur = con.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS Student (ROLL_NUMBER INT PRIMARY KEY, NAME CHAR(50),AGE INT,GENDER varchar(50),TOTAL_MARK FLOAT,RANK INT)') 
                try:
                        cur.execute("INSERT INTO Student (ROLL_NUMBER, NAME, AGE, GENDER, TOTAL_MARK, RANK) VALUES(?, ?, ?, ?, ?, ?)", (ROLL_NUMBER, NAME, AGE, GENDER, TOTAL_MARK, RANK))
                        print ("RECORD ADDED SUCCESSFULLY !!!")
                        con.commit()
                except sqlite3.IntegrityError:
                        print("Roll Number already exists")
                con.close() 

                
        def delete_data(self,ROLL_NUMBER):
                self.ROLL_NUMBER = ROLL_NUMBER
                con = sqlite3.connect('studentDB.db')
                cur = con.cursor()
                cur.execute("SELECT COUNT(*) FROM Student where ROLL_NUMBER=?",(ROLL_NUMBER,))
                row=cur.fetchone()
                row_count=row[0]
                if row_count == 0:
                        print("Roll Number doesn't exist")
                else:
                        cur.execute("DELETE FROM Student where ROLL_NUMBER=?",(ROLL_NUMBER,))
                        print("RECORD DELETED SUCCESSFULLY !!!")
                        con.commit()
                con.close()


        def update_data(self,ROLL_NUMBER,NAME,AGE,GENDER,TOTAL_MARK,RANK):
                con = sqlite3.connect('studentDB.db')
                cur = con.cursor()
                self.ROLL_NUMBER = ROLL_NUMBER
                self.NAME = NAME
                self.AGE = AGE
                self.GENDER = GENDER
                self.TOTAL_MARK = TOTAL_MARK
                self.RANK = RANK
                cur.execute("SELECT COUNT(*) FROM Student where ROLL_NUMBER=?",(ROLL_NUMBER,))
                row=cur.fetchone()
                row_count=row[0]
                if row_count == 0:
                        print("Roll Number doesn't exist")
                else:
                        cur.execute("UPDATE Student SET ROLL_NUMBER= ? , NAME= ? , AGE= ? , GENDER= ? , TOTAL_MARK= ? , RANK= ?  WHERE ROLL_NUMBER= ? ", (ROLL_NUMBER, NAME, AGE, GENDER, TOTAL_MARK, RANK,ROLL_NUMBER))
                        print ("RECORD UPDATED SUCCESSFULLY !!!")
                        con.commit()
                con.close()

        def view_data(self):
                con = sqlite3.connect('studentDB.db')
                cur = con.cursor()
                cur.execute("SELECT * FROM Student ORDER BY ROLL_NUMBER ASC")
                rows=cur.fetchall()
                for row in rows:
                        print("ROLL NUMBER : ",row[0])
                        print("NAME : ",row[1])
                        print("AGE : ",row[2])
                        print("GENDER : ",row[3])
                        print("TOTAL MARKS : ",row[4])
                        print("RANK : ",row[5])
                        print("\n")
                con.close()


        def search_data(self,ROLL_NUMBER):
                self.ROLL_NUMBER = ROLL_NUMBER
                con = sqlite3.connect('studentDB.db')
                cur = con.cursor()
                cur.execute("SELECT COUNT(*) FROM Student where ROLL_NUMBER=?",(ROLL_NUMBER,))
                row=cur.fetchone()
                row_count=row[0]
                if row_count == 0:
                        print("Roll Number doesn't exist")
                else:
                        cur.execute("SELECT * FROM Student where ROLL_NUMBER=?",(ROLL_NUMBER,))
                        rows=cur.fetchall()
                        for row in rows:
                                print("ROLL NUMBER : ",row[0])
                                print("NAME : ",row[1])
                                print("AGE : ",row[2])
                                print("GENDER : ",row[3])
                                print("TOTAL MARKS : ",row[4])
                                print("RANK : ",row[5])
                con.close()

obj=Student()

def print_menu():
    print (30 * "-" , "STUDENT MANAGEMENT SYSTEM" , 30 * "-")
    print ("1. ADD STUDENTS")
    print ("2. DELETE STUDENTS")
    print ("3. MODIFY STUDENTS")
    print ("4. LIST STUDENTS")
    print ("5. SEARCH STUDENT")
    print ("6. EXIT")
    print (87 * "-")
  
loop=True      
  
while loop:          
    print_menu()    
    choice = int(input("Enter your choice [1-6]: "))
     
    if choice==1:     
        print("\nADD STUDENT DETAILS.")
        print("--------------------\n")

        try:
              ROLL_NUMBER=int(input("Enter Roll Number : "))
        except ValueError:
                print("Roll Number must be a NUMBER")
                continue
        
        NAME=input("Enter Name : ")
        if NAME.replace(" ", "").isalpha():
                pass
        else:
                print("Enter a valid NAME")
                continue
        try:
                AGE=int(input("Enter Age : "))
        except ValueError:
                print("Age must be a NUMBER")
                continue
                
        GENDER=input("Enter Gender (M/F): ")
        if GENDER.isalpha():
                pass
        else:
                print("Enter a valid GENDER")
                continue
        try:
                TOTAL_MARK=float(input("Enter Total Marks : "))
        except ValueError:
                print("Total Mark must be a NUMBER")
                continue
        try:
                RANK=int(input("Enter Rank : "))
        except ValueError:
                print("Rank must be a NUMBER")
                continue
        
        obj.insert_data(ROLL_NUMBER,NAME,AGE,GENDER,TOTAL_MARK,RANK)
        
    elif choice==2:
        print("\nDELETE STUDENT DETAILS.")
        print("-----------------------\n")
        try:
              ROLL_NUMBER=int(input("Enter Roll Number to delete : "))
        except ValueError:
                print("Roll Number must be a NUMBER")
                continue
        obj.delete_data(ROLL_NUMBER) 
        
    elif choice==3:
        print("\nMODIFY STUDENT DETAILS")
        print("----------------------\n")
        try:
              ROLL_NUMBER=int(input("Enter Roll Number to modify : "))
        except ValueError:
                print("Roll Number must be a NUMBER")
                continue
        
        NAME=input("Enter Name : ")
        if NAME.replace(" ", "").isalpha():
                pass
        else:
                print("Enter a valid NAME")
                continue
        try:
                AGE=int(input("Enter Age : "))
        except ValueError:
                print("Age must be a NUMBER")
                continue
                
        GENDER=input("Enter Gender (M/F): ")
        if GENDER.isalpha():
                pass
        else:
                print("Enter a valid GENDER")
                continue
        try:
                TOTAL_MARK=float(input("Enter Total Marks : "))
        except ValueError:
                print("Total Mark must be a NUMBER")
                continue
        try:
                RANK=int(input("Enter Rank : "))
        except ValueError:
                print("Rank must be a NUMBER")
                continue
        obj.update_data(ROLL_NUMBER,NAME,AGE,GENDER,TOTAL_MARK,RANK) 
        
    elif choice==4:
        print("\nLIST STUDENT DETAILS")
        print("--------------------\n")
        obj.view_data()
        
    elif choice==5:
        print("\nSEARCH STUDENT DETAILS")
        print("----------------------\n")
        try:
              ROLL_NUMBER=int(input("Enter Roll Number to search : "))
        except ValueError:
                print("Roll Number must be a NUMBER")
                continue
        obj.search_data(ROLL_NUMBER)
            
    elif choice==6:
        print("Exiting...")
        loop=False
        
    else:
        
        print("Wrong option selected. Enter a valid option [1-6]:")

