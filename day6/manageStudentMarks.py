subjects=("Maths","English","Science")

students_names=set()

students_marks={}



def recursive_total(marks_list):
    if len(marks_list)==0:
        return 0
    return marks_list[0]+recursive_total(marks_list[1:])



def add_student():
        try:
             name=input("enter student name: ")
             marks=[]
             for subject in subjects:
                  mark=int(input(f"enter marks for {subject}: "))
                  marks.append(mark)
                  students_names.add(name)
                  students_marks[name]=marks
        except ValueError:
                  print("Invalid input! Please enter numeric marks.")
        except TypeError:
                  print("marks data type error")


def display_students():
       for name,marks in students_marks.items():
             print (name,":", marks)


def calculate_average():
      try:
            name=input("Enter student name to calculate: ")
            if name not in students_marks:
              raise NameError
            marks_list=students_marks[name]
            total=recursive_total(marks_list)
            print("total marks",total)
            avg=total/len(marks_list)
            print("Average marks:",avg)
      except NameError:
            print("student name not found")
      except ZeroDivisionError:
        print("can't divide by zero")
      except TypeError:
            print("type data error")




while True:
      print("4 options")
      print("1.Add Student")
      print("2.Display Students")
      print("3.calculate average")
      print("4.exit")
      
      
      choice=int(input("enter your choice: "))
      if choice==1:
        add_student()
      elif  choice==2:
        display_students()
      elif  choice==3:
           calculate_average()
      elif choice ==4:
           break
      else:
           "invalid"
           
   

    
            
