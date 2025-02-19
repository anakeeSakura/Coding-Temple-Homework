nested_dict = {
    "person1": {
        "name": "Alice",
        "age": 30,
        "address": {
            "street": "123 Elm St",
            "city": "Wonderland",
            "zipcode": "12345"
        },
        "hobbies": ["reading", "cycling", "painting"]
    },
    "person2": {
        "name": "Bob",
        "age": 25,
        "address": {
            "street": "456 Oak St",
            "city": "Buildertown",
            "zipcode": "67890"
        },
        "hobbies": ["gaming", "hiking", "photography"]
    }
}

# grab these values for person 1 and person 2

# grab name

# print(f"This is the name: {nested_dict["person1"]["name"]}")

# # grab age
# print(f"This is the age: {nested_dict["person1"]["age"]}")
# # grab the address city
# print(f"This is the address city: {nested_dict["person1"]["address"]['city']}")
# # grab the address street
# print(f"This is the address street: {nested_dict['person1']['address']['street']}")
# # grab the address zipcode
# print(f"This is the address zipcode: {nested_dict['person1']['address']['zipcode']}")
# # grab each individual hobby
# print(f"This is the hobby: {nested_dict["person1"]["hobbies"][0:3]}")
# for hobby in nested_dict ["person1"]["hobbies"]:
#     print(f"This is the hobby: {hobby}")

# for key, value in nested_dict["person1"].items():
#     # print(f"Key: {key}, Value: {value}")
#     # if key == "name":
#     #     print(f"this is the age: {nested_dict['person1'][key]}")
#     if key == "address":
#         print(f"this is the address: {nested_dict['person1'][key]['street']}")

# the_age = int(input("Enter age: "))

# for key, value in nested_dict["person1"].items():
#     if key == "age":
#         if the_age == nested_dict['person1'][key]:
#             print(f"this is the age: {nested_dict['person1'][key]}")

# for key, value in nested_dict["person1"].items():
#     if key == "hobbies":
#         print(f"this is the hobby: {nested_dict['person1'][key][1]}")



# 
# for key, value in nested_dict.items():
#     print(f"Key: {key}")
#     print(f"value: {value}")
print(f"This is the name : {nested_dict["person2"]["name"]}")

print(f"This is the age: {nested_dict["person2"]["age"]}")

print(f"This is the address street: {nested_dict["person2"]["address"]["street"]}")

print(f"This is the city: {nested_dict["person2"]["address"]["city"]}")

print(f"This is the zipcode: {nested_dict['person2']["address"]["zipcode"]}")

print(f"This is the hobbies: {nested_dict['person2']['hobbies']}")

print(f" this is hobby 1: {nested_dict['person2']['hobbies'][0]}")
print(f" this is hobby 2: {nested_dict["person2"]['hobbies'][1]}")
print(f" this is hobby 3: {nested_dict['person2']["hobbies"][2]}")


print("hello world".upper())