import requests
from urllib.request import urlopen
import json

def look_for_person():
    name = input("enter the first name of the person: ")
    url = "http://192.168.29.84:5000/api?first_name={}".format(name)

    try:
        content = urlopen(url)

        data = json.load(content)
        for i in data:
            print(i + ":"+str(data[i]))
    except Exception as ex:
        print("The person is not in your database pls check again")

def add_to_database():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    age = input('Age: ')
    gender = input("Gender: ")
    email= input("Email: ")
    phone_no = input('Phone number: ')
    relation = input("Relation: ")

    url= f"http://192.168.29.84:5000/api/add?first_name={first_name}&last_name={last_name}&age={age}&gender={gender}&email={email}&phone_no={phone_no}&relation={relation}"

    try:
        content = urlopen(url)
        data = json.load(content)
        print(data)
    except Exception as ex:
        print(ex)



