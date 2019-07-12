
import mysql.connector as cnt
from colorama import Fore as f, Style as s


mydb=cnt.connect(host="localhost",user="root",passwd="Shazx06@",database="test_db")
cursor=mydb.cursor()
cursor.execute('''
create table  if not exists students(
ID int primary key auto_increment ,
name varchar(100),
branch varchar(100),
section varchar(100),
math_marks float ,
py_marks float ,
sql_marks float ,
total_marks float )
'''
)


def student_input():

 std_i=int(input('enter the no of stundents u want to take input:  '))
 
 for i in range(std_i):
     
    id(i)
    Name=str(input('enter the name:  ')).upper()
    branch=input("enter the branch: ").upper()
    sectin=input("enter the section: ").upper()
    mth=float(input("enter the maths marks:   "))
    py=float(input("enter the python marks:  "))
    sql=float(input('enter the sql marks:  '))
    total_marks=(mth+py+sql)
    
    
    cursor.execute(f'insert into students(name,branch,section,math_marks,py_marks,sql_marks,total_marks) \
    values("{Name}","{branch}","{sectin}",{mth},{py},{sql},{total_marks})')
    mydb.commit()





'''student output'''

def student_output():
 
 cursor.execute('select * from students')
 result=cursor.fetchall()
 if result==[]:
     print('\nempty no data to show\n')
 else:
     print('information of students ')
     print(f'{s.BRIGHT}{f.YELLOW}')
     print(" ID           NAME          branch       section    MATH         PYTHON        SQL       TOTAL_MARKS")
     
     print(f"{s.RESET_ALL}{f.YELLOW}",end="")
 


 for i,j,k,l,m,n,o,p in result:
         print(f'{i:3}    {j:>10}          {k:>6}        {l:>5}     {m:.3f}       {n:.3f}       {o:.3f}       {p:.3f}')
 print(f'{s.RESET_ALL}')
 



def student_manipulation():
     id=int(input("input the id of student for which you want to manipulate marks:"))
     
     print("\nDATA before manipulation\n")
     print(f'{s.BRIGHT}{f.YELLOW}')
     print(" ID           NAME          branch       section    MATH         PYTHON        SQL       TOTAL_MARKS")
     
     print(f"{s.RESET_ALL}{f.YELLOW}",end="")
     cursor.execute(f"select * from students where id={id}  ")
     result=cursor.fetchall()
    


     for i,j,k,l,m,n,o,p in result:
         print(f'{i:3}    {j:>10}          {k:>6}        {l:>5}     {m:.3f}       {n:.3f}       {o:.3f}       {p:.3f}')
     print(f'{s.RESET_ALL}')
     
     x=int(input('press 1 if want to change section else press 0 '))
     if x==1:
             sec=input('input the new section: ').upper()
             cursor.execute(f'update students set section="{sec}" where id={id}')
             mydb.commit()
             

     x1=int(input('press 1 if want to change maths marks else press 0  '))
     if x1==1:
             mth=float(input('input the new maths_marks: '))
             cursor.execute(f'update students set math_marks={mth} where id={id}')
             mydb.commit() 
             

     x2=int(input('press 1 if want to change py_marks else press 0  '))
     if x2==1:
             mth=float(input('input the new py_marks: '))
             cursor.execute(f'update students set py_marks={mth} where id={id}')
             mydb.commit()
             

     x3=int(input('press 1 if want to change sql marks else press 0:  '))
     if x3==1:
             mth=float(input('input the new sql_marks: '))
             cursor.execute(f'update students set sql_marks={mth} where id={id}')
             mydb.commit()
     cursor.execute(f"update students set total_marks=math_marks+sql_marks + py_marks where id={id}")
     mydb.commit()
     print("\nDATA before manipulation\n")
     print(f'{s.BRIGHT}{f.YELLOW}')
     print(" ID           NAME          branch       section    MATH         PYTHON        SQL       TOTAL_MARKS")
     
     print(f"{s.RESET_ALL}{f.YELLOW}",end="")
     cursor.execute(f"select * from students where id={id}  ")
     result=cursor.fetchall()
    


     for i,j,k,l,m,n,o,p in result:
         print(f'{i:3}    {j:>10}          {k:>6}        {l:>5}     {m:.3f}       {n:.3f}       {o:.3f}       {p:.3f}')
     print(f'{s.RESET_ALL}')
    

     

def highest_marks():
    cursor.execute('select * from students order by total_marks desc limit 1')
    result=cursor.fetchall()
    
    print(f'{s.BRIGHT}{f.YELLOW}')
    print(" ID           NAME          branch       section    MATH         PYTHON        SQL       TOTAL_MARKS")
    print(f"{s.RESET_ALL}{f.YELLOW}",end="")
     
    for i,j,k,l,m,n,o,p in result:
         print(f'{i:3}    {j:>10}          {k:>6}        {l:>5}     {m:.3f}      {n:.3f}       {o:.3f}       {p:.3f}')
    
    
    
    print(f'{s.RESET_ALL}')


def lowest_marks():
    cursor.execute('select * from students order by total_marks limit 1')
    result=cursor.fetchall()
    
    print(f'{s.BRIGHT}{f.YELLOW}')
    print(" ID           NAME          branch       section    MATH         PYTHON        SQL       TOTAL_MARKS")
    
    print(f"{s.RESET_ALL}{f.YELLOW}",end="")


    for i,j,k,l,m,n,o,p in result:
         print(f'{i:3}    {j:>10}          {k:>6}        {l:>5}     {m:.3f}       {n:.3f}       {o:.3f}       {p:.3f}')
    print(f'{s.RESET_ALL}')



def failed_students():
    cursor.execute("select * from students where (total_marks<105 or py_marks<35 or math_marks<35 or sql_marks<35)")
    result=cursor.fetchall()
    print(f'{s.BRIGHT}{f.YELLOW}')
    print(" ID           NAME          branch       section    MATH         PYTHON        SQL       TOTAL_MARKS")
    print(f"{s.RESET_ALL}{f.YELLOW}",end="")


    for i,j,k,l,m,n,o,p in result:
         print(f'{i:3}    {j:>10}          {k:>6}        {l:>5}     {m:.3f}       {n:.3f}       {o:.3f}       {p:.3f}')
    print(f'{s.RESET_ALL}')


def student_search():
   z=True
   print('\ndo you want to search by name or id\n')
   while(z==True) :
    
    x=int(input("input 0 for name and 1 for id search:  "))
    if x==0:
        z=False
        Name=input('enter the name:  ').upper()
        print()
        cursor.execute(f"select * from students where name ='{Name}'")
        result=cursor.fetchall()

    elif x==1:

        z=False
        id=int(input("enter the ID:  "))
        print()
        cursor.execute(f"select * from students where id={id}")
        result=cursor.fetchall()
    else: 
        print("CHOOSE OPTION WISELY")
        continue
    print(f'{s.BRIGHT}{f.YELLOW}')
    print(" ID           NAME          branch       section    MATH         PYTHON        SQL       TOTAL_MARKS")
    print(f"{s.RESET_ALL}{f.YELLOW}",end="")


    for i,j,k,l,m,n,o,p in result:
         print(f'{i:3}    {j:>10}          {k:>6}        {l:>5}     {m:.3f}       {n:.3f}       {o:.3f}       {p:.3f}')
    print(f'{s.RESET_ALL}')



def high_sub():
    print("\ndetail of all subjects topper\n")
    cursor.execute("select id, name ,math_marks from students order by math_marks desc limit 1")
    result1=cursor.fetchall()
    
    cursor.execute("select id, name , sql_marks from students order by sql_marks desc limit 1")
    result2=cursor.fetchall()
    
    cursor.execute("select id , name , py_marks from students order by py_marks desc limit 1")
    result3=cursor.fetchall()
    ree=[result1,result2,result3]

    for t in ree:
        if id(t)==id(result1):
            print(f"{f.BLUE}\nmaths topper\n{s.RESET_ALL}")
        if id(t)==id(result2):
            print(f"{f.BLUE}\nsql topper\n{s.RESET_ALL}")
        if id(t)==id(result3):
            print(f"{f.BLUE}\npython topper\n{s.RESET_ALL}")

        for i,j,k in t:
            print(f'{s.BRIGHT}{f.YELLOW}',end="")
            print(" ID           NAME         subject marks")
            print(f"{s.RESET_ALL}{f.YELLOW}",end="")
         
            print(f'{i:3}    {j:>10}          {k:>6}    ')
            print(f'{s.RESET_ALL}')






def section_info():
    
    print("info accoring to section")
    
    cursor.execute('select section , count(*), round(avg(total_marks ),2) from students group by section ')
    result=cursor.fetchall()
    print(f'{s.BRIGHT}{f.YELLOW}')
    print("SECTION  STUDENT_COUNT   AVG_CLS_SCR")
    print(f"{s.RESET_ALL}{f.YELLOW}",end="")
    for i , j, k in result:
        print(f'{i:>6}           {j}            {k}')
    print(f'{s.RESET_ALL}')


    
def sec_stud():
    print("\nprinting the student name section wise")
    cursor.execute('select section from students group by section ')
    result1=cursor.fetchall()
    for i  in result1:
        
        i=i[0]
        cursor.execute(f'select id,name from students where section="{i:3}"')
        print(f"\n{f.MAGENTA}{s.BRIGHT}The Students Of Section : {i:3}{s.RESET_ALL}\n")
        result=cursor.fetchall()
        print(f"{f.YELLOW}{s.BRIGHT}",end="")


        print(' ID          NAME',end="")
        print(f"{s.RESET_ALL}",end="")
        print(f"{f.YELLOW}")

        for i , j in result:
                  print(f'{i:3}     {j:>10}')
        print(f"{s.RESET_ALL}",end="")
    
                  
def delete():
  z=True
  print("deleting info of student by ID or NAME: \n")
  while z==True:
    
    x=int(input("press 0 for name and 1 for id delete:  "))
    if x==0:
        z=False
        Name=input("enter the name of student to be deleted: ").upper()
        try:
          cursor.execute(f"delete from students where name='{Name}'")
          mydb.commit()
          print(f"\n{f.BLUE}Information have been successfully deleted from database: {s.RESET_ALL}")
        except :
            print(f"{f.RED}oops something went wrong{s.RESET_ALL}")      

    elif x==1:

    

        z=False
        id=int(input("enter the id of student to be deleted:   "))
        try:
            cursor.execute(f"delete from students where id={id}")
            mydb.commit()
            print(f"\n{f.BLUE}Information have been successfully deleted from database: {s.RESET_ALL}")
        except :
          print(f"{f.RED}oops something went wrong{s.RESET_ALL}")        
    else: 
        print("CHOOSE OPTION WISELY")
        
        continue

 







