from colorama import Fore,Style,init
from datetime import date
from note import Note

noteslist=[]


while True:
    user=input(
            (Fore.LIGHTGREEN_EX+"1. add new\n" ) + 
            (Fore.CYAN+"2. note search\n")+
            (Fore.BLACK+"3. list notes\n")+
            Style.RESET_ALL)

    if user == "1":
        t=input("Please Title this note, AI cant do everything for you: ")
        d=input("Enter the description and stop scrolling through tiktok: ")
        da= date.today().strftime("%m/%d/%Y")
        ii=input("is this note important, if you say it isnt thats my dinner (y/n): ")

        if ii=="y":
            ii=True
        else:
            ii=False

        note=Note(t,d,da,ii)
        noteslist.append(note)







# note1 = Note("Testing","test unit","4/4/2025",True)
# note2 = Note("test unit" , "Testing" , "68/98/2300",False)

# print(note1.title)
# print(note2.desc)