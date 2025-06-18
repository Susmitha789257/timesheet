from tabulate import tabulate
import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Susmitha@789",
    database="Daily_Time_Sheet_2025"
)
cursor=conn.cursor()
class Daily_Time_Sheet:
    def __init__(self):
        print("WELCOME TO DAILY TIME SHEET PORTAL\n")
        actions=[("EXIT"),("INSERT"),("UPDATE"),("VIEW"),("DELETE")]
        self.actions=[[i,actions[i]] for i in range(len(actions))]
        levels=[("BACK"),("BASIC"),("INTERMEDIATE"),("ADVANCED"),("EXPERT"),("ADDITIONAL")]
        self.levels=[[i,levels[i]] for i in range(len(levels))]
    def Actions(self):
        print(tabulate(self.actions,headers=["OPTION","ACTION"],tablefmt="fancy_grid"))
    def Levels(self):
        print(tabulate(self.levels,headers=["LEVEL","ACTION"],tablefmt="fancy_grid"))
    def Choice(self):
        self.choice=int(input("\nPlease Enter Your Option : "))
        return self.choice
app=Daily_Time_Sheet()
def TaskMenu(choice):
    sql="select TASK from DailyTimeTable where LEVEL=%s"
    cursor.execute(sql,(choice,))
    task=cursor.fetchall()
    task.insert(0,["BACK"])
    task=[[i,task[i][0]] for i in range(len(task))]
    print(tabulate(task,headers=["S.NO","TASK"],tablefmt="fancy_grid"))
    temp=app.Choice()
    if temp==0:
        LevelMenu()
    elif temp in [1,2]:
        percent=int(input("Please enter your GYM WORKOUT completion percentage: "))
        print("Wonderful")
        print(task[temp][1])
    else:
        print("Oops! Invalid option. Please enter a valid option and try again!")
        TaskMenu(choice)
    
def LevelMenu():
    app.Levels()
    choice=app.Choice()
    if choice==0:
        MainMenu()
    elif choice in range(1,5):
        TaskMenu(choice)
    else:
        print("Oops! Invalid option. Please enter a valid option and try again!")
        LevelMenu()
def MainMenu():
    app.Actions()
    choice=app.Choice()
    if choice==0:
        print("🙏 THANK YOU FOR USING THE DAILY TIME SHEET - PLEASE COME AGAIN! 🙏")
        quit()
    elif choice==1:
        LevelMenu()
    else:
        print("Oops! Invalid option. Please enter a valid option and try again!")
        MainMenu()
MainMenu()
<<<<<<< HEAD
print("this is update version123")
=======
print("this is update version")
>>>>>>> f4caed3763c4cfd01a487fac77f5656f6e9b3197

##while True:
##    app.Actions()
##    choice=app.Choice()
##    if choice==0:
##        print("THANK YOU")
##        quit()
##    elif choice==1:
##        while True:
##            app.Levels()
##            choice=app.Choice()
##            if choice==0:
##                continue
##            elif choice in range(1,5):
##                while True:
##                    sql="select TASK from DailyTimeTable where LEVEL=%s"
##                    cursor.execute(sql,(choice,))
##                    task=cursor.fetchall()
##                    task.insert(0,["BACK"])
##                    task=[[i,task[i][0]] for i in range(len(task))]
##                    print(tabulate(task,headers=["S.NO","TASK"],tablefmt="fancy_grid"))
##                    choice1=app.Choice()
##                    if choice1==0:
##                        continue
##                    else:
##                        print("Oops! Invalid choice. Please try again.")
##                        break
##            else:
##                print("Oops! Invalid choice. Please try again.")
##    elif choice==2:
##        pass
##    elif choice==3:
##        pass
##    elif choice==4:
##        pass
##    else:
##        print("Oops! Invalid choice. Please try again.")
cursor.close()
conn.close()
      

##def Action():
##    action=[("EXIT"),("INSERT"),("UPDATE"),("VIEW"),("DELETE")]
##    action=[[i,action[i]] for i in range(len(action))]
##    print(tabulate(action,headers=["OPTION","ACTION"],tablefmt="fancy_grid"))
##Action()
##option=int(input("\nPlease Enter Your Option : "))
##def Level():
##    level=[("BACK"),("BASIC"),("INTERMEDIATE"),("ADVANCED"),("EXPERT")]
##    level=[[i,level[i]] for i in range(len(level))]
##    print(tabulate(level,headers=["LEVEL","ACTION"],tablefmt="fancy_grid"))
##if option==0:
##    print("THANK YOU")
##    quit()
##elif option==1:
##    Level()
##    option1=int(input("\nPlease Enter Your Option : "))
##elif option==2:
##   pass
##elif option==3:
##   pass
##elif option==4:
##   pass
##else:
##    print("Oops! Invalid choice. Please try again.")
##
##from tabulate import tabulate
##import mysql.connector
##conn=mysql.connector.connect(
##    host="localhost",
##    user="root",
##    password="Susmitha@789",
##    database="Daily_Time_Sheet_2025"
##)
##cursor=conn.cursor()
##sql="""SELECT TASK
##FROM DailyTimeTable where level=1;
##"""
##cursor.execute(sql)
##rows = cursor.fetchall()
####rows=rows + [
####    ('11:30 AM', '12:30 PM', 'Project', '1H'),
####    ('12:30 PM', '01:00 PM', 'Lunch', '30M')
####]
##S_NO = [[i + 1] + list(row) for i, row in enumerate(rows)]
##S_NO = [[i+1]+list(rows[i]) for i in range(len(rows))]
###print(rows)
##print(tabulate(S_NO, headers=["S.NO", "START", "END", "TASK", "HOURS/MINUTES"], tablefmt="fancy_grid"))
##
##
##
##
##
##conn.close()
