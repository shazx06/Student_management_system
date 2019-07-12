# author -shaibs
from functions import *
print(f"\n{f.RED}FORGET ABOUT ' ' FOR SQL STRING SYNTAX WE MANUAULLY ADDED IN PROGRAM{s.RESET_ALL}")



y=True
while y==True:
  print('''
press 1. for student data input...
press 2. for student data output...
press 3. for student data manipulation...
press 4. detail of student with highest marks...
press 5. detail of students with lowest marks...
press 6. detail of student who failed i.e. less than 35% either in total or in any subject...
press 7. search student info by id or name...
press 8. detail toppers subject wise...
press 9  details of sections...
press 10. for printing the name and id of student sectin wise...
press 11. to delete information of a student 
            
    ''')
  x=int()
  try: 
     x=int(input("enter your choice:   "))
  except :
      print(f"\n{f.RED}please input only digits{s.RESET_ALL}\n")
      x=int(input("enter your choice wisely:  "))
      
  if x==1:
      student_input()
  elif x==2:
      student_output()
  elif x==3:
      student_manipulation()
  elif x==4:
     highest_marks()
  elif x==5:
      lowest_marks()
  elif x==6:
      failed_students()
  elif x==7:
      student_search()
  elif x==8:
      high_sub()
  elif x==9:
      section_info()
  elif x==10:
      sec_stud()
  elif x==11:
      delete()
  else:
      print("\nplease input a valid option from a list\n")
  ch=input("\nif you want to continue press yes/y else press any key:  ")
  if ch.lower()=="yes" or ch.lower()=='y':
      
      continue
  else:
      import sys
      print(f"\n\n{f.MAGENTA} SEE YOU LATER{s.RESET_ALL}\n\n")
      sys.exit()
