nested_dict = {
    "person1": {
        "name": "Alice",
        "age": 30,
        "address": {
            "street": "123 Elm St",
            "city": "Wonderland",
            "zipcode": "12345",
            "coordinates": {
                "latitude": 51.5074,
                "longitude": -0.1278
            }
        },
        "hobbies": ["reading", "cycling", "painting"],
        "employment": {
            "status": "Employed",
            "position": "Software Engineer",
            "company": "TechWorks Inc.",
            "years_of_experience": 8
        },
        "contacts": [
            {"type": "email", "value": "alice@wonderland.com"},
            {"type": "phone", "value": "555-1234"}
        ]
    },
    "person2": {
        "name": "Bob",
        "age": 25,
        "address": {
            "street": "456 Oak St",
            "city": "Buildertown",
            "zipcode": "67890",
            "coordinates": {
                "latitude": 40.7128,
                "longitude": -74.0060
            }
        },
        "hobbies": ["gaming", "hiking", "photography"],
        "employment": {
            "status": "Self-Employed",
            "position": "Freelance Photographer",
            "projects": [
                {"name": "Nature Series", "status": "Completed", "year": 2023},
                {"name": "Urban Exploration", "status": "In Progress", "year": 2024}
            ]
        },
        "contacts": [
            {"type": "email", "value": "bob@buildertown.com"},
            {"type": "phone", "value": "555-6789"}
        ]
    },
    "person3": {
        "name": "Charlie",
        "age": 35,
        "address": {
            "street": "789 Pine St",
            "city": "Techville",
            "zipcode": "11223",
            "coordinates": {
                "latitude": 37.7749,
                "longitude": -122.4194
            }
        },
        "hobbies": ["traveling", "swimming", "photography"],
        "employment": {
            "status": "Employed",
            "position": "Data Scientist",
            "company": "DataX Solutions",
            "years_of_experience": 10,
            "skills": ["Python", "Machine Learning", "Data Visualization"]
        },
        "contacts": [
            {"type": "email", "value": "charlie@techville.com"},
            {"type": "phone", "value": "555-9876"}
        ]
    }
}

print(f"This is the contact {nested_dict['person2']["contacts"][1]["value"]}")

print(f"This is person 2 photos {nested_dict['person2']['employment']["projects"][0]["name"]}")

print(f"This is person 1 coordinates {nested_dict["person1"]["address"]["coordinates"]["latitude"]}")

# person_number = input("Enter the Person number: ")
# # print("person" + person_number) 
# print(f"The Hobby {nested_dict["person" + person_number]["hobbies"][1]}")

# person_number = input("Enter the Person number: ")
# print(f"{nested_dict["person" + person_number]["employment"]}")
# for key, value in nested_dict["person" + person_number]["employment"].items():
#     # print(f"{key}\n{value}")
#     if key == "company":
#         print(value)
#         break

# person_number = input("Enter the Person number: ") 
# address_choice = input("Enter the person location info choice: ") 
# # print(f"{nested_dict['person' + person_number]["address"]}")
# for key, value in nested_dict['person' + person_number]["address"].items():
#     if key == address_choice:
#         print(value)
         
# print(f"This is the address {nested_dict['person2']["address"]["street"]}")
# nested_dict['person2']["address"]["street"] = "3515 Canyon Pkwy apt 7308"
# print(f"This is the address {nested_dict['person2']["address"]["street"]}")
# print(f"This is the address {nested_dict['person2']["address"]}")
def method():
    person_number = input("Enter the Person number: ")
    for key, value in nested_dict["person" + person_number]["employment"].items():
        # print(f"{key}\n{value}")
        if key == "position":
            print(value)
            nested_dict["person" + person_number]["employment"][key] = input("Enter New position: ")
            print(f"This is the new position {nested_dict['person' + person_number]['employment'][key]}")

method()

method()

