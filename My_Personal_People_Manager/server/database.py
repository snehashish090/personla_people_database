# Database file
import os
import json

with open("data/names.json", "r") as file:
    data = json.load(file)

# Function to create a new database
def setup_database():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(f"data/names.json"):
        with open(f"data/names.json", "w") as file:
            json.dump([], file, indent=True)
    else:
        pass

class Person:

    def __init__(self, first_name, last_name, age, gender, email, phone_no, relation = "None" ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email = email
        self.phone_no  = phone_no
        self.realtion = relation

    def get_info_dict(self):
        return {
            "first_name":self.first_name,
            "last_name":self.last_name,
            "age":self.age,
            "gender":self.gender,
            "email":self.email,
            "phone_no":self.phone_no,
            "relation":self.realtion
        }

    def get_info_print(self):
                print(f"""
        First Name:{self.first_name},
        Last Name:{self.last_name},
        Age:{self.age},
        Gender:{self.gender},
        Email Adress:{self.email},
        Phone Number:{self.phone_no},
        Relation:{self.realtion}
        """)

def fetch_all():

    if data != []:
        list_of_people = []

        for i in data:
            person = Person(
                i["first_name"],
                i["last_name"],
                i["age"],
                i["gender"],
                i["email"],
                i["phone_no"],
                i["relation"]
            )
            list_of_people.append(person)

        for i in list_of_people:
            print(i.get_info_print())
    else:
        print("No People in ur contacts!")


def add_to_database(first_name, last_name, age, gender, email, phone_no, relation):
    with open("data/names.json", "w") as file:
        person = Person(
                first_name,
                last_name,
                age,
                gender,
                email,
                phone_no,
                relation
            )
        data.append(person.get_info_dict())
        json.dump(data, file, indent=4)