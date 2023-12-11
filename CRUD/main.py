import json
import os




def create():
    user_list = []
    name = input("Type your name: ")
    email = input("Type your email: ")
    age = int(input("Type your age: "))
    address = input("Type your address: ")
    phone = input("Type your phone: ")
    user = {"name": name, "age": age,"email":email,"address": address, "phone": phone}
    user_list.append(user)

    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            existing_data = file.read()  # Read the content of the file as a string
            if existing_data:
                existing_data = json.loads(existing_data)
                print(existing_data)
                user_list.extend(existing_data)
            else:
                print("No existing data found in users.json")
    with open("users.json" , "w") as file:
        json.dump(user_list , file)
        
    print("user data saved successfully!")

def read():
    with open("users.json", "r") as file:
        existing_data = file.read()  # Read the content of the file as a string
        if existing_data:
            existing_data = json.loads(existing_data)
            for user in existing_data:
                print(f"Name:{user['name']}\nEmail:{user['email']}\nAge:{user['age']}\nAddress:{user['address']}\nPhone:{user['phone']}\n=============")
        else:
            print("No existing data found in users.json")


def delete():
    name = input("type name: ")
    with open("users.json", "r") as file:
        existing_data = file.read()  # Read the content of the file as a string
        if existing_data:
            existing_data = json.loads(existing_data)
            user_found = False

            for user in existing_data:
                if name.lower() == user["name"].lower():
                    existing_data.remove(user)
                    user_found= True
                    break
            if not user_found:
                print("user not found")
                
        else:
            print("No existing data found in users.json")
            
    with open("users.json" , "w") as file:
        json.dump(existing_data , file)
        print("User data deleted successfully!")

def update():
    name = input("type name: ")
    with open("users.json", "r") as file:
        existing_data = file.read()  # Read the content of the file as a string
        if existing_data:
            existing_data = json.loads(existing_data)
            user_found = False

            for user in existing_data:
                if name.lower() == user["name"].lower():
                    email = input("Enter updated email: ")
                    phone = input("Enter updated contact: ")

                    # Update the user data
                    user["email"] = email
                    user["phone"] = contact
                    user_found= True
                    break
            if not user_found:
                print("user not found")
                
        else:
            print("No existing data found in users.json")
            
    with open("users.json" , "w") as file:
        json.dump(existing_data , file)
        print("User data updated successfully!")
    
create()   
read()
delete()
update()
