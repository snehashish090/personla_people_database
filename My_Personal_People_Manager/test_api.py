import requests


def look_for_person():
    name = input("enter the first name of the person: ")
 
    try:
        api2 = requests.get("http://192.168.29.84:5000/api?first_name={}".format(name))
        i = api2.json()

        print("First Name: ", i["first_name"])
        print("Last Name: ",i["last_name"])
        print("Age: ", i["age"])
        print("Gender: ", i["gender"])
        print("Email Adress: ", i["email"])
        print("Phone Number: ", i["phone_no"])
        print("Relation: ", i["relation"])

    except:
        print("Sorry but the person is not in the database")

look_for_person()