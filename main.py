from colorama import Fore,Style,init
from datetime import date
from note import Note

noteslist=[]

with open("datapal.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        noteinfo=line.split(",")
        title=noteinfo[0]
        desc=noteinfo[1]
        d=noteinfo[2]
        ii=noteinfo[3]
        ot=noteinfo[4]
        
        if ii=="True":
            ii=True
        else:
            ii=False
            
        if ot=="True":
            ot=True
        else:
            ot=False

        note=Note(title,desc,d,ii,ot)
        noteslist.append(note)



def safetybud():
    #title,desc,date,importance
    with open("datapal.txt","w") as file:
        file.write("")
    
    for note in noteslist:
        if note.isonetime==False:
            with open("datapal.txt","a") as file:
                result=f"{note.title},{note.desc},{note.date},{note.isimportant},{note.isonetime}\n"
                file.write(result)


while True:
    user=input(
            (Fore.LIGHTGREEN_EX+"1. add new\n" ) + 
            (Fore.CYAN+"2. note search\n")+
            (Fore.BLACK+"3. list notes\n")+
            (Fore.RED+"4. delete notes\n")+
            Style.RESET_ALL)

    if user == "1":
        t=input("Please Title this note, AI cant do everything for you: ")
        d=input("Enter the description and stop scrolling through tiktok: ")
        da= date.today().strftime("%m/%d/%Y")
        ii=input("is this note important, if you say it isnt thats my dinner (y/n): ")
        io=input("ARE YOU SURE YOU WANT TO DELETE THIS NOTE!!! (y/n): ")
        if ii=="y":
            ii=True
        else:
            ii=False

        if io=="y":
            io=True
        else:
            io=False

        note=Note(t,d,da,ii,io)
        noteslist.append(note)
        safetybud()
    elif user == "2":
        t=input("Select a title, and do your homework: ")
        for i in noteslist:
            if i.title==t:
                print(i)
    elif user == "3":
        for i in noteslist:
            print(i)
    elif user =="4":
        title=input("salutations user,This app requests that thou select a role to vainquish: ")
        for i in range(len(noteslist)):
            if noteslist[i].title == title:
                noteslist.pop(i)
        safetybud()

        









# note1 = Note("Testing","test unit","4/4/2025",True)
# note2 = Note("test unit" , "Testing" , "68/98/2300",False)

# print(note1.title)
# print(note2.desc)