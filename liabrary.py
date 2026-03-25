import json
import random
import string
from pathlib import Path
from datetime import datetime


class Liabrary:
    database = "Liabrary.json"
    data = {"books": [] , "members":[]}

    #Load existing data to json

    if Path(database).exists():
        with open(database,"r") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)
            else:
                with open(database,'w') as f:
                    json.dump(data,f,indent=4)






    def gen_id(prefix = "B"):
        random_id = ""
        for i in range(5):
            random_id += random.choice(string.ascii_uppercase + string.digits)
            return prefix + "-" + random_id
    @classmethod    
    def save_data(cls):
        with open(cls.database,'w')as f:
            json.dump(cls.data,f,indent=4,default=str)


    def add_book(self):
        title =input("Enter book title :")
        author = input("Enter the book author :")
        copies = int(input("how many copies :"))

        book = {
            "id" : Liabrary.gen_id(),
            "title" : title,
            "author": author,
            "total copies" : copies,
            "available_copies" : copies,
            "added_on" : datetime.now().strftime("%Y&-m-%d %H:%M:%S")

        }
        Liabrary.data['books'].append(book)
        Liabrary.save_data()


    def list_books(self):
        if not Liabrary.data['books']:
            print("sorry no books found")
            return
        for b in Liabrary.data['books']:
            print(f"{b['id']:12} {b['title'] [:24]:25} {b['author'][:19]:20} {b['total copies']/b['available_copies']:>3}")
            print()

    def add_member(self):
        name = input("Enter the name:-")
        email = input("please enter the email:-")

        member = {
            "id" : Liabrary.gen_id("M"),
            "name" : name,
            "email" : email,
            "borowed" : []

        }
        Liabrary.data['members'].append(member)
        Liabrary.save_data()
        print("Member added sucessfully")

    def list_members(self):
        if not Liabrary.data['members']:
            print('there are no members')
            return
        for m in Liabrary.data['members']:
            print(f"{m['id']:12} {m['name'][:24]:25} {m['email'][:29]:30}")
            print("this guy has currently")
            print(f"{m['borowed']}")
            print()

    def borrow(self):
        member_id = input("enter the member ID :").strip()
        members = [m for m in Liabrary.data['members'] if m['id'] == member_id] 
        if not members:
            print("no such ID exists")
            return
        member = members[0]

        book_id = input("enter the book id :")
        books = [b for b in Liabrary.data['books'] if b['id'] == book_id]

        if not books:
            print("sorry no such id of book exist")
            return
        book = books[0]

        if book['avaliable_copies'] <= 0:
            print("sorry no books exist")
            return
        
        borrow_entry = {
            "book_id" : book['id'],
            "title" : book['title'],
            "borrow_on" :  datetime.now().strftime("%Y&-m-%d %H:%M:%S")
        }

        member = ['borowed'].append(borrow_entry)
        book['available_copies'] -=1
        Liabrary.save_data()

    def return_book(self):
        member_id = input("Enter the member ID:").strip()
        members = [m for m in Liabrary.data['members'] if m ['id'] == member_id]
        if not members:
            print("no such ID exist")
            return
        member = members[0]
        if not member['borowed']:
            print("no borowed books")
            return
        print("borowed books")
        for i, b in enumerate(member['borowed'],start = 1):
            print(f"{i}. {b['title']} ({b['book_id']})")

            try:
                choice = int(input("enter number to return :-"))
                selected = member['borowed'].pop(choice - 1)
            except Exception as err:
                print("invalid value")

            books = [bk for bk in Liabrary.data['books'] if bk[id] == selected['book_id'] ]
            if books:
                books[0]['available_copies'] += 1

            Liabrary.save_data()












        

hello = Liabrary()

while True:

    print("="*50)
    print("Liabrary Management System")
    print("="*50)
    print("1.Add Book")
    print("2.List Books")
    print("3.Add Members")
    print("4.List Members")
    print("5.Borrow Book")
    print("6.Return Book")
    print("0.Exit the Portal")
    print("="*50)
    choice = input("what task you want to do")

if choice == "1":
    hello.add_book()

if choice == "2":
    hello.list_books()

if choice == "3":
    hello.add_member()

if choice == "4":
    hello.list_members()

if choice == "5":
    hello.borrow()

if choice == "6":
    hello.return_book()

if choice == "0":
    exit(0)

