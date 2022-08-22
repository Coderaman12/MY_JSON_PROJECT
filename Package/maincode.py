from enum import Flag
import json
from pathlib import Path
import random
import re
import string
import os
from threading import ExceptHookArgs
from turtle import update

# class 
class Management:
    __database="Package/final_challenge_project.json"          # database 
    __info=[]                                                # list in database
    try:
        if not Path(__database).exists:                      # database open 
            with open (__database,'w') as fw:
                fw.write(json.dumps(__info))
        else:
            with open(__database,'r') as fr:
                __info=json.loads(fr.read())
    except Exception as err:
        print("ERROR >> ",err)
    # function for generate id 
    def __generateid(self):
        seq1=(random.choices(string.ascii_letters,k=3))
        seq2=(random.choices(string.digits,k=3))
        seq3=(random.choices(list('@#$*'),k=2))
        x=seq1+seq2+seq3
        random.shuffle(x)
        return ("".join(x))
    #1.function for insert data 
    def __InsertData(self):
        try:
            __data={}
            __data["id"]=self.__generateid()
            __data["name"]=input("Enter Full Name : ").strip().lower()
            __data["status"]=input("Enter status (Student/Teacher): ").strip().lower()
            __data["contact"]=int(input("Enter contact number: ").strip())
            __data["email"]=input("Enter Email: ")
            Management.__info.append(__data)
            with open(Management.__database,'w') as fw:
                fw.write(json.dumps(Management.__info))
                print(f"\nName >> {__data['name']}\nID >> {__data['id']}\n")
                return f"REGISTERED SUSSESFULLY!\n-- please !!! note down your id to access again --\n"
        except Exception as err:
            print("\nERROR FROM INSERT PART >> ",err)
    #2.1 .Read Single data
    def __Read_SingleStu_Data():
        try: 
            flag=True
            __id=input("\nEnter Your ID:")
            with open(Management.__database) as f:
                    __data=json.load(f)
            for i in __data:
                if __id==i["id"]:
                    flag=False
                    print(f"\nData >> {i}")
            if flag==True:
                print("\nThis 'ID' Data not Found !\n")
        except Exception as err:
            print("\nERROR FROM READ_SINGLE_DATA >> ",err)
    #2.2  read from the key  
    def __ReadSameKey():
        __key=input("\nEnter the Key(ID,Name,Status,Contact,Email): ").strip().lower()
        try:
            with open(Management.__database) as f:
                __data=json.load(f)
            print()
            for i,v in enumerate(__data):
                print(f"{i+1}.Data for Key {__key} >> {v[__key]}\n")
            return f""
        except Exception as err:
            print("\nERROR FROM READ SAME KEY >> ",err)
    #2.3 for single unit data
    def __ReadUnit():
        id=input("Enter ID: ")
        key=input("Enter the key(name,status,contact): ").strip().lower()
        try:
            with open (Management.__database) as f:
                __data=json.load(f)
                for v in (__data):
                    if v['id']==id:
                        print(f"\nData of id = {id} and type = {key} >> {v[key]}")
        except Exception as err:
            print("\nERROR FROM READ UNIT >> ",err)
    #2.4 for same type of name.status,contact,email
    def __Same_Data():
        __key=input("Enter the Key (Name,Status,Contact,Email): ").strip().lower()
        __value=input(f"Enter {__key}: ").strip().lower()
        try:
            with open (Management.__database) as f:
                __data=json.load(f)
                count=0
                for i in (__data):
                    if __value==i[__key]:
                        count+=1
                print(f"\nTotal {__key} >> {count} ")
        except Exception as er:
            print("\nERROR FROM SAME DATA >> ",er)
    #2 read data
    def __READ_DATA(self):
        while True:
            __ask=int(input("\n1.Read Single Student/Teacher all Data\n2.Read all Keyvalue Data\n3.Single Unit Data\n4.Read Same Value Data\n0.For Exit\nChoose any one option: "))
            if __ask==1:
                Management.__Read_SingleStu_Data()
            elif __ask==2:
                print(Management.__ReadSameKey())
            elif __ask==3:
                Management.__ReadUnit()
            elif __ask==4:
                Management.__Same_Data()
            elif __ask==0:
                print("\nExit From Read(2) loops\n")
                break
            else:
                    print("\n-- WRONG INPUT --\n")
#5
    def __ReadAll(self):
        __pas=input("\nEnter the passward which was given by developer:\n").strip()
        if __pas=="12345":
            try:
                with open(Management.__database) as f:
                    __data=json.load(f)
                    count=0
                    for i,v in enumerate(__data):
                        print(f"{i+1} >> {v}\n")
                        count+=1
                    print(f"Total members are >> {count}\n")
            except Exception as err:
                print("\nERROR FROM READ ALL >> ",err)
        else:
            print("-- WRONG PASSWORD --")
# update class method
    @classmethod
    def UpdateData(cls):
        try:
            with open(cls.__database,'r') as fr:
                cls.__info=json.loads(fr.read())
        except Exception as err:
            print("\nERROR FROM UPDATEDDATA >> ",err)
    #4.1
    def __FiledataDelete():
        try:
            flag=False
            id=input("\nEnter Employe ID: ")
            with open(Management.__database)as f:
                __data=json.load(f)
                for i in __data:
                    if id==i['id']:
                        flag=True
            if flag==True:
                filteredemps=[
                    data for data in Management.__info if data['id']!=id]
                with open(Management.__database,'w') as fw:
                    fw.write(json.dumps(filteredemps))
                Management.UpdateData()
                print(f"\nData Delected!\n")
            else:
                print(f"\n-- DATA NOT FOUND! --\n")
        except Exception as err:
            print("\nERROR FROM FILEDATADELECE >> ",err)
    #4.2 empty the json file
    def __EmptyJson():
        try:
            __pas=input("\nEnter the passward which was given by developer:").strip()
            if __pas=="12345":
                __emptyjson=[]
                with open(Management.__database,'w') as fw:
                    fw.write(json.dumps(__emptyjson))
                Management.UpdateData() 
                print(f"\n EMPTY OF JSON FILE IS COMPLETED!\n")
            else:
                print("\n-- WRONG PASSWARD --\n")    
        except Exception as err:
            print("\nERROR FROM EMPTY JSON >> ",err)
    #4.3 delete json file
    def __DeleteJson():
        try:
            __pas=input("\nEnter the passward which was given by developer:").strip()
            if __pas=="12345":
               os.remove(Management.__database)
               print("-- JSON FILE DELETED --")
            else:
                print("\n-- WRONG PASSWARD --\n")    
        except Exception as err:
            print("\nERROR FROM DELETE JSON >> ",err)
    #4 delete file
    def __Delete(self):
        while True:
            __ask=int(input("1.File Data Deleted by use of ID\n2.Empty JSON File\n3.Delete JSON File\n0.EXIT \nchoose any one option: "))
            if __ask==1:
                Management.__FiledataDelete()    
            elif __ask==2:
                Management.__EmptyJson()
            elif __ask==3:
                Management.__DeleteJson()
            elif __ask==0:
                print("\nExit fron Delete loop\n")
                break
            else:
                print("\n--WRONG INPUT --\n")
#3
    def __FileUpdate(self):
        try:
            flag=True
            __id=input("\nEnter Your ID:")
            with open(Management.__database) as f:
                    __data=json.load(f)
            for i in __data:
                if __id==i["id"]:
                    flag=False
                    print(f"\nData >> {i}")
            if flag==True:
                print("\nThis 'ID' Data not Found !\n")
            for i,v in enumerate(Management.__info):
                if __id==v['id']:
                    print("SKIP BY PRESSING ENTER ")
                    updatedinfo={}
                    updatedinfo['name']=input("Enter Updated Name ")
                    updatedinfo['status']=input("Enter Updated status ")
                    updatedinfo['contact']=input("Enter Updated contact number ")
                    updatedinfo['email']=input("Enter Updated Email: ")
                    if not updatedinfo['name'].strip():
                        del updatedinfo['name']
                    if not updatedinfo["status"].strip():
                        del updatedinfo["status"]
                    if not updatedinfo["contact"].strip():
                        del updatedinfo["contact"]
                    if not updatedinfo["email"].strip():
                        del updatedinfo['email']
                    Management.__info[i]={**v,**updatedinfo}
                    with open(Management.__database,'w') as fw:
                        fw.write(json.dumps(Management.__info))
                    Management.UpdateData()
                    return f"\nINFORMATION WITH ID {v['id']} HAS BEEN UPDATED SUCCESFULLY!\n"
            return f"\nDATA NOT FOUND!\n"
        except Exception as err:
            print("ERROR >> ",err)
    #5 EXIT FROM LOOP
    def __Exit(self):
        print(f"\n------ HELLO WORLD ------\n")
# main def to control the program
    def Main(self):
        while True:
            print("1.Insert data of student/teacher")
            print("2.Read Single data of student/teacher ('id' is required)")
            print("3.Update data of student/teacher ('id' is required)")
            print("4.Delete data of student/teacher ('id' is required)")
            print("5.Read all data from jsons (password required: )")
            print("0.Exit Application")
            try:
                n=int(input("Enter Your choice: "))
                if n==1:
                    res.__InsertData()
                elif n==2:
                    res.__READ_DATA()
                elif n==3:
                    res.__FileUpdate()
                elif n==4:
                    res.__Delete()
                elif n==5:
                    res.__ReadAll()
                elif n==0:
                    res.__Exit()
                    break
            except Exception as err:
                print("ERROR >> ",err)
# main
res=Management()
main=res.Main()

