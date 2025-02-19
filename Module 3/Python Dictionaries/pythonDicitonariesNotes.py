#  '''''
# kitchen = { "Spoons" : "Top Drawer ", "Forks" : "Middle Drawer", "Knives" : "Bottom Drawer" }
# print(kitchen)
# set key value (spoons,forks, knives) to represent different kitchen items.
# set value (top drawer, middle drawer, bottom drawer) to specify the designated storage location for each item.
# Use a colon to separatge each key from its corresponding value.  Use a comma to separate each key-value pair. Use curly brackets to enclose the entire dictionary.
# kitchen = { "Spoons" : "Top Drawer ", "Forks" : "Middle Drawer", "Knives" : "Bottom Drawer" }
# location_of_spoons = kitchen[ "Spoons"]
#  print(location_of_spoons)
# use the key "Spoons" to access the value associated with it, which is "Top Drawer

# # # # # # # # # # # # # # # # '''Handling Missing Keys 
# # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # kitchen = { "Spoons" : "Top Drawer ", "Forks" : "Middle Drawer", "Knives" : "Bottom Drawer" }

# # # # # # # # # # # # # # # location_of_toaster  = kitchen[ "Toaster"]
# # # # # # # # # # # # # # # # print(location_of_toaster)  # This will raise a KeyError
# # # # # # # # # # # # # # # # To avoid this, you can use the get() method, which returns None if the key is

# # # # # # # # # # # # # # # '''safely accesing elements with get() '''
# # # # # # # # # # # # # # # kitchen = { "Spoons" : "Top Drawer ", "Forks" : "Middle Drawer", "Knives" : "Bottom Drawer" }
# # # # # # # # # # # # # # # location_of_toaster =  kitchen.get("Toaster",  "Not Found")
# # # # # # # # # # # # # # # print(location_of_toaster)  # Output: Not Found

# # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # adding and updating elements in python dictionaries'''

# # # # # # # # # # # # # # # community_center = {"Yoga": "8 AM", "Art":  "10 AM", "Music": "2 PM" }

# # # # # # # # # # # # # # # community_center["Cooking"] = "1 PM"
# # # # # # # # # # # # # # # print(community_center)

# # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # The Art of updating: Modifying  existing values '''

# # # # # # # # # # # # # # # community_center = {"Yoga": "8 AM", "Art":  "10 AM", "Music": "2 PM" }
# # # # # # # # # # # # # # # community_center["Art"] = "11 AM"
# # # # # # # # # # # # # # # print(community_center)

# # # # # # # # # # # # # # # '''The pop() Method'''
# # # # # # # # # # # # # # # inventory = {"Apples": 30, "Oranges": 20, "Grapes": 50}
# # # # # # # # # # # # # # # removed_item  = inventory.pop("Apples")
# # # # # # # # # # # # # # # print(removed_item) 

# # # # # # # # # # # # # # # '''The del keyword'''
# # # # # # # # # # # # # # # book_shelf = {"Fiction": 10,  "Non-Fiction": 20, "Biography": 30}
# # # # # # # # # # # # # # # del book_shelf[""]
# # # # # # # # # # # # # # # print(book_shelf)\
# # # # # # # # # # # # # # # # Output: {'Fiction': 10, 'Non-Fiction': 20, 'Biography': 30}

# # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # The clear()method'''
# # # # # # # # # # # # # # # session_data =  {"username": "John", "password": "1234", "email": "john@example.com "}
# # # # # # # # # # # # # # # session_data.clear()
# # # # # # # # # # # # # # # print(session_data)  # Output: {} session_data is now  an empty dictionary

# # # # # # # # # # # # # # # ''' 
# # # # # # # # # # # # # # # The items() Method'''
# # # # # # # # # # # # # # # book_ratings = {"1984": 4.5, "To Kill a mockingbird":4.8,  "Pride and Prejudice": 4.2 }
# # # # # # # # # # # # # # # for i, j in book_ratings.items():
# # # # # # # # # # # # # # #     print(f"{j} has a rating of {i}")


# # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # The keys() Method'''
# # # # # # # # # # # # # # # user_profile =  {"name": "John", "age": 30, "city": "New York" }
# # # # # # # # # # # # # # # for key in user_profile.keys():
# # # # # # # # # # # # # # #     print(key)

# # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # Looping Through a Dictionary keys in a particular order
# # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # colors_count =  {"Red": 5, "Blue": 10, "Green": 15 }
# # # # # # # # # # # # # # # for color in sorted (colors_count.keys()):
# # # # # # # # # # # # # # #     print(f"{color}: {colors_count[color]}")

# # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # The update Method'''

# # # # # # # # # # # # # # # default_settings =  {"theme": "light", "font_size": 12 }
# # # # # # # # # # # # # # # custom_settings = {"theme": "dark", "font_size": 14, "language": " Spanish" }
# # # # # # # # # # # # # # # default_settings.update(custom_settings)
# # # # # # # # # # # # # # # print(default_settings)   # Output: {'theme': 'dark', 'font_size': 14, 'language': 'Spanish' }


# # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # The setdefault Method 
# # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # stock =  {"Apple": 10, "oranges": 20}
# # # # # # # # # # # # # # # stock.setdefault("bananas", 0)
# # # # # # # # # # # # # # # print(stock.setdefault("apples"))    # Output: 10

# # # # # # # # # # # # # # # print(stock)   # Output: {'Apple': 10, 'oranges': 20, 'bananas ': 0 }

# # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # Shallow copy: The photographic Duplicate
# # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # original_artists  =  {"Picasso": 1881, "Van Gogh": 1853,"Monet": 1840}
# # # # # # # # # # # # # # # copied_artists = original_artists.copy()
# # # # # # # # # # # # # # # test_artists = original_artists


# # # # # # # # # # # # # # # Changing a value in the copied dictionary
# # # # # # # # # # # # # # # copied_artists["Van Gogh"] = 1900
# # # # # # # # # # # # # # # print("Original:", original_artists)  # Original remains unchanged
# # # # # # # # # # # # # # # print("Copied:", copied_artists)  # Copied reflects the change
# # # # # # # # # # # # # # # print("Test:", test_artists)  # Test also reflects the change


# # # # # # # # # # # # # # '''Deep Copy: The Independent Reproduction'''
# # # # # # # # # # # # # # import  copy
# # # # # # # # # # # # # # original_paintings =   {"The Starry Night": "Van Gogh", "The Scream": "Munch" }
# # # # # # # # # # # # # # reproduced_painting = copy.deepcopy(original_paintings)

# # # # # # # # # # # # # # # Changing a value in the copied dictionary
# # # # # # # # # # # # # # reproduced_painting["The Starry Night"] = "Da  Vinci"
# # # # # # # # # # # # # # print("Original:", original_paintings) #Original remains unchanged
# # # # # # # # # # # # # # print("Reproduced:", reproduced_painting) #Reproduced reflects the change


# # # # # # # # # # # # # '''How Changes Can Affect the original? Shallow Copy'''
# # # # # # # # # # # # # # Original exhibit informaiton
# # # # # # # # # # # # # museum_exhibit = {"Ancient Vase": ["Greece", "Egypt"], "Renanissance Painting":  ["Italy", "France"]}

# # # # # # # # # # # # # # Creating a shallow copy
# # # # # # # # # # # # # exhibit_copy = museum_exhibit.copy()

# # # # # # # # # # # # # # Creating a shallow copy
# # # # # # # # # # # # # exhibit_copy = museum_exhibit.copy()

# # # # # # # # # # # # # # Adding a new country to the "Ancient Vase" list in the copied dictionary
# # # # # # # # # # # # # exhibit_copy["Ancient Vase"].append("China")

# # # # # # # # # # # # # print("Original Exhibit:", museum_exhibit)
# # # # # # # # # # # # # print("Copied Exhibit:", exhibit_copy)


# # # # # # # # # # # # '''
# # # # # # # # # # # # The Library Shelf
# # # # # # # # # # # # '''
# # # # # # # # # # # # library = { "Fantasy": ["Harry Potter", "The Hobbit"], 
# # # # # # # # # # # #             "Science Fiction": ["Dune", "1984"],
# # # # # # # # # # # #             "Romance": ["Pride and Prejudice", "The Notebook"] 
# # # # # # # # # # # # }
           
# # # # # # # # # # # # library["Fantasy"].append("The Name of the Wind")
# # # # # # # # # # # # # print(library)
# # # # # # # # # # # # # Output: {'Fantasy': ['Harry Potter', 'The Hobbit', 'The Name of  the Wind'], 'Science Fiction': ['Dune', '1984'], 'Romance': [' Pride and Prejudice', 'The Notebook']}

# # # # # # # # # # # # for book in library["Science Fiction"]:
# # # # # # # # # # # #     print(book)

# # # # # # # # # # # # for genre, books in library.items():
# # # # # # # # # # # #     print(f"Genre: {genre}")
# # # # # # # # # # # #     for book in books:
# # # # # # # # # # # #         print(f" -  {book}")


# # # # # # # # # # # '''
# # # # # # # # # # # Exploring the Gallery
# # # # # # # # # # # '''
# # # # # # # # # # # art_gallery = [ 
# # # # # # # # # # #     {"title": "The Starry Night", "artist": "Vincent van Gogh",  "year": 1889},
# # # # # # # # # # #     {"title": "The Mona Lisa", "artist": "Leonardo da Vinci", "year ": 1503},
# # # # # # # # # # #     {"title": "The Scream", "artist": "Edvard Munch", "year ": 1893}
# # # # # # # # # # # ]
# # # # # # # # # # # art_gallery.append({"Title": "The Persistence of memory",  "Artist": "Salvador Dali", "Year": 1931})

# # # # # # # # # # # for artwork in art_gallery:
# # # # # # # # # # #     print(f"Title: {artwork['title']}, Artist: {artwork['artist ']}, Year: {artwork['year']}")


# # # # # # # # # # # """Example: Art Pieces in a Gallery"""
# # # # # # # # # # # art_gallery =  [
# # # # # # # # # # #     {"title": "The Starry Night", "artist": "Vincent van Gogh",   "year": 1889},
# # # # # # # # # # #     {"title": "The Mona Lisa", "artist": "Leonardo da Vinci", "year ": 1503},
# # # # # # # # # # #     {"title": "The Scream", "artist": "Edvard Munch", "year  ": 1893} 
# # # # # # # # # # #     ]
# # # # # # # # # # # # Adding a new art piece to the gallery
# # # # # # # # # # # art_gallery.append({"title": "The Persistence of memory", "artist": "Salvador Dali", "year": 1931})
# # # # # # # # # # # # Iterating over the art pieces in the gallery
# # # # # # # # # # # for artwork in art_gallery:
# # # # # # # # # # #     print(f"Title: {artwork['title']}, Artist: {artwork['artist ']}, Year: {artwork['year']}") 
# # # # # # # # # # #     # Output:  Title: The Starry Night, Artist: Vincent van Gogh, Year: 1889 

# # # # # # # # # # ''''
# # # # # # # # # # Exploring the layers: A Museum's Themed Exhibits
# # # # # # # # # # '''
# # # # # # # # # # museum_exhibits =  {
# # # # # # # # # #     "Ancient Egypt":{
# # # # # # # # # #         "Artifacts":["Sphinx", "Pyramids"],
# # # # # # # # # #         "Famous Pharaohs" : ["Tutankhamun", "Cleopatra"]     
# # # # # # # # # #     },
# # # # # # # # # # "Renaissance Art": {
# # # # # # # # # #     "Notable Artists": ["Leonardo da Vinci", "Michelangelo"],
# # # # # # # # # #     "Key Works":  ["Mona Lisa", "The Last Supper"]
# # # # # # # # # #     }
# # # # # # # # # # }

# # # # # # # # # # museum_exhibits["Ancient Egypt"]["Recent Discoveries"] = ["New Tomb", "Ancient Scrolls"]
# # # # # # # # # # #print(museum_exhibits)

# # # # # # # # # # for exhibit, details in museum_exhibits.items():
# # # # # # # # # #     print(f"Exhibit: {exhibit}")
# # # # # # # # # #     for section, items in details.items():
# # # # # # # # # #         print(f"  {section}: {', '.join(items)}")

# # # # # # # # # '''
# # # # # # # # # Exercise 1: E-commerce Product Catalog Management

# # # # # # # # # Develop a Python to manage a product catalog for an e-commerce platform.
# # # # # # # # # The program should faciliteate adding new product categories, adding products to existing categories, displaying all available categories,
# # # # # # # # # and searching for product within the catalog. 

# # # # # # # # # 1. Initialize a dictionary to represent the product catalog.
# # # # # # # # # 2. Implement functions for: 
# # # # # # # # # - Adding a new product category. 
# # # # # # # # # - Adding a product to an existing category. 
# # # # # # # # # - Displaying all categories and their respective products.
# # # # # # # # # - Searching for a product across all categories (case-insensitive).
# # # # # # # # # 3. Use exception handling to address potential errors, such as adding products to non-existent categories.
# # # # # # # # # 4. Implement case - insensitive search functionality for product queries.

# # # # # # # # # Hints:
# # # # # # # # # -Start with a pre-populated dictionary for eas of testing.
# # # # # # # # # -Utilize string methods like 'lower() for case-insensitive comparisons.
# # # # # # # # # - In the search function, interate through all catgegories to find the product.
# # # # # # # # # - Implement 'try' and 'except' blocks to gracefully handle situations where a specified category does not exist in the catalog.

# # # # # # # # # '''
# # # # # # # # # def add_category(catalog, category):
# # # # # # # # #     if category not in catalog:
# # # # # # # # #         catalog[category] = []
# # # # # # # # #         print(f"Category '{category}' added.")
# # # # # # # # #     else:
# # # # # # # # #         print(f"Category '{category}' already exists.")

# # # # # # # # # def add_product(catalog, category, product):
# # # # # # # # #     try:
# # # # # # # # #         if product not in catalog[category]:
# # # # # # # # #             catalog[category].append(product)
# # # # # # # # #             print[f"Product '{product}' added to '{category}'."]
# # # # # # # # #     except KeyError:
# # # # # # # # #         print(f"Category '{category}' does not exist.")

# # # # # # # # # catalog =  {
# # # # # # # # #     "Electronics": ["Smartphone", "Laptop", "Tablet"],
# # # # # # # # #     "Books":  ["Fiction", "Non-Fiction", "Biography"],
# # # # # # # # # }

# # # # # # # # # add_category(catalog, "Clothing")

# # # # # # # # # print(catalog)

# # # # # # # # """Exercise 2: Social Media Content Organizer
# # # # # # # # Develop a Python program to manage and organize sicial media content. 
# # # # # # # # The program should categorize posts into different social media platforms (e.g., Facebook, Instagram),
# # # # # # # # and further categorieze these posts into types (e.g., Text, Image, Video).

# # # # # # # # 1. Create a nested dictionary where the first level represtns social media platforms and the sedonc level categoriezed the types of posts.
# # # # # # # # 2. Implement functions to: 
# # # # # # # # -Add a new social media platform to the dictionary. 
# # # # # # # # -Add a new post type to a specific platform. 
# # # # # # # # -Add a post to a specific type within a platform. 
# # # # # # # # -Display all platforms, post types, and posts.

# # # # # # # # 3. Ensure that the program can handle adding new platforms and post types dynamically.

# # # # # # # # -Initialize your dictionary with a least two platforms and a few post types.
# # # # # # # # -Use a nested loops to iterate through the platforms and their post types when displaying content.
# # # # # # # # -Implement checks to handle the addition of alreadyu existing platforms or post types.
# # # # # # # # """
# # # # # # # # def add_platform(content_dict, platform):
# # # # # # # #     if  platform not in content_dict:
# # # # # # # #         content_dict[platform] = {}
# # # # # # # #         print(f"Platform '{platform}' added.")
# # # # # # # #     else:
# # # # # # # #         print(f"platform '{platform}' already exists.")

# # # # # # # # def add_post_type(content_dict, platform, post_type):
# # # # # # # #     if platform not in content_dict:
# # # # # # # #         if post_type not in content_dict[platform]:
# # # # # # # #             content_dict[platform][post_type] = []
# # # # # # # #             print(f"Post type '{post_type}' added to '{platform}'.")
# # # # # # # #         else:
# # # # # # # #             print(f"Post type '{post_type}' already exists in '{platform}'.")
# # # # # # # #     else:
# # # # # # # #         print(f"Platform '{platform}' does not exist.")

# # # # # # # # def add_post(content_dict,platform, post_type, post):
# # # # # # # #     if platform in content_dict and post_type in content_dict[platform]:
# # # # # # # #         content_dict[platform][post_type].append(post)
# # # # # # # #         print(f"Post added to '{platform}' under '{post_type}'.")
# # # # # # # #     else:
# # # # # # # #         print(f"Either platform '{platform}' or post type  '{post_type}' does not exist.")

# # # # # # # # def display_content(content_dict):
# # # # # # # #     for platform, post_types in content_dict.items():
# # # # # # # #         print(f"Platform:  {platform}")
# # # # # # # #         for post_type, posts in post_types.items():
# # # # # # # #             print(f"Post Type: {post_type}")
# # # # # # # #             for post in posts:
# # # # # # # #                 print(f"   - {post}")

# # # # # # # # social_media_content =  {
# # # # # # # #     "Facebook":  {
# # # # # # # #         "Text": ["Hello World", "Python is fun!"],
# # # # # # # #         "Image": ["Beach photo", "Birthday party"],
# # # # # # # #     }
# # # # # # # # }

# # # # # # # # add_platform(social_media_content, "Instagram")
# # # # # # # # add_post_type(social_media_content, "Facebook",  "Video")
# # # # # # # # add_post(social_media_content, "Instagram", "image", "Sunset view")
# # # # # # # # display_content(social_media_content)

# # # # # # # '''
# # # # # # # Exercise 3: Restuaruant Menu and Order Management 
# # # # # # # Create a Python program to manage a restaurant's menu and customer orders.
# # # # # # # The program should allow for menu management (add/removing items and categories) and handling customers orders by selecting items from the menu.

# # # # # # # Instructions:

# # # # # # # 1. Define a dictioinary to represent the restuarants's menu, with categoires as keys and list of menu items as values.
# # # # # # # 2. Implement funtions for:
# # # # # # # -Adding and removing menu categories.
# # # # # # # -Adding and removing items within a category.
# # # # # # # -Taking a customer's order by  selecting items from the menu.
# # # # # # # -Displaying the menu and customer's order.
# # # # # # # 3. Include error handling for cases liek attmepting to order an item not an item not on the menu.

# # # # # # # Hints:
# # # # # # # Start with a pre-defined menu.
# # # # # # # Use 'try and except for handling invalid order requests.
# # # # # # # consider using a list to store individual customer orders.
# # # # # # # '''

# # # # # # # def add_category(menu,  category):
# # # # # # #     if category not in menu:
# # # # # # #         menu[category] =  []
# # # # # # #         print(f"Category '{category}' added to the menu.")
# # # # # # #     else:
# # # # # # #         print(f"Category '{category}' already exists in the menu.")

# # # # # # # def add_item(menu, category, item):
# # # # # # #     if category in menu: #if beverages in restuarant_menu
# # # # # # #         if item not in menu[category]:
# # # # # # #             menu[category].append(item)
# # # # # # #             print(f"Item '{item}' added to category '{category}'.")
# # # # # # #         else:
# # # # # # #             print(f"Item '{item}' already exists in category '{category}'.")
# # # # # # #     else: print(f"Category '{category}' does not exist.")

# # # # # # # def take_order(menu, order):
# # # # # # #     try:
# # # # # # #         order_items  = [menu[category][item_index] for category, item_index in order]
# # # # # # #         return order_items
# # # # # # #     except (KeyError, IndexError):
# # # # # # #         print("Invalid order. Please check menu and order again.")
# # # # # # #         return None

# # # # # # # def display_menu(menu):
# # # # # # #     for category, items in menu.items():
# # # # # # #         print(f"{category}: {', '.join(items)}")

# # # # # # # resturant_menu =  {
# # # # # # #     "Starter":["Soup","Salad"],
# # # # # # #     "Main Course":["Burger","Pizza","Sandwich"],
# # # # # # #     "Dessert":["Cake", "Ice Cream"]
# # # # # # #     }
# # # # # # # add_category(resturant_menu, "Beverages")
# # # # # # # add_item(resturant_menu, "Beverages", "Water")
# # # # # # # customer_order = [("Main Course", 1), ("Dessert",0)] # Ordering Pizza and Cake
# # # # # # # order_items = take_order(resturant_menu, customer_order)
# # # # # # # if order_items:
# # # # # # #     print("Customer order:", order_items)
# # # # # # # display_menu(resturant_menu)

# # # # # # '''
# # # # # # Exercise 4: Hotel Room Booking System

# # # # # # Develop a system to track and manage room bookings for a hotel.
# # # # # # The program should allow adding rooms, chekcing room availability, booking rooms, and displaying current bookings.

# # # # # # Instructions:
# # # # # # 1. Use a dictionary to represent the hotel rooms, where keys are room numbers and values are boolean indicating availability.
# # # # # # 2. Implement functions for:
# # # # # # -Adding new rooms to the hotel.
# # # # # # -Checking if a room is available.
# # # # # # -Booking a room.
# # # # # # -Displaying all room and their current status.  
# # # # # # 3. Incorporate a main loop that allows users to choose different actions (e.g., add room, book room, etc.).
# # # # # # 4. Use exception handl,ing for invalid inputs or actions, such as attempting to book an already occupied room.

# # # # # # Hints:
# # # # # # Intilialize your dictionary with a set of rooms.
# # # # # # Use a while loop fo rthe pain program execution, allowing continous operation until the user decides to exit.
# # # # # # Use a while loop for the main program execution, allowing continous operation until the user deices to exit.
# # # # # # When booking, check the room's availability before confirming the booking. '''

# # # # # # def add_room(hotel, room_number):
# # # # # #     if  room_number not in hotel:
# # # # # #         hotel[room_number] = True # True indicates the room is available
# # # # # #         print(f"Room {room_number} added successfully.")
# # # # # #     else:
# # # # # #         print(f"Room {room_number} already exists in the hotel.")

# # # # # # def is_available(hotel, room_number):
# # # # # #     return hotel.get(room_number, False)

# # # # # # def book_room(hotel, room_number):
# # # # # #     if is_available(hotel, room_number):
# # # # # #         hotel[room_number] = False # False indicates the room is occupied
# # # # # #         print(f"Room {room_number} booked successfully.")
# # # # # #     else:
# # # # # #         print(f"Room {room_number} is not available.")

# # # # # # def  display_rooms(hotel):
# # # # # #      for room, available in hotel.items():
# # # # # #         status = "Available" if available else "Occupied"
# # # # # #         print(f"Room {room}: {status}")

# # # # # # hotel_rooms = {"101": True,  "102": False, "103": True}

# # # # # # while True:
# # # # # #     print("\nHotel Management System")
# # # # # #     print("1: Add Room\n2: Book Room\n3: Check Room Availability\n4:Display Rooms\n5:Exit")
# # # # # #     choice = input("Enter your choice: ")

# # # # # #     if choice == "1":
# # # # # #         room = input("Enter room number to add: ")
# # # # # #         add_room(hotel_rooms, room)
# # # # # #     elif  choice == "2":
# # # # # #         room = input("Enter room number to book: ")
# # # # # #         book_room(hotel_rooms, room)
# # # # # #     elif choice ==  "3":
# # # # # #         room = input("Enter room number to check availability: ")
# # # # # #         available = is_available(hotel_rooms, room)
# # # # # #         print(f"Room {room} is {'available' if available else 'not available'}")
# # # # # #     elif choice  == "4":
# # # # # #         display_rooms(hotel_rooms)
# # # # # #     elif  choice == "5":
# # # # # #         print("Exiting the program. Goodbye!")
# # # # # #         break
# # # # # #     else:
# # # # # #         print("Invalid choice. Please choose a valid option.")

# # # # # '''
# # # # # Exercise 5: customer Feedback Analysis for a product
# # # # # Create a system to categorize and count customer feedback based on sntiment (postive, negative, neutral) for a specific 
# # # # # product. The program should allow adding new feedback

# # # # # 1. Use a dictionary to store customer feedback, categorized by sentiment.
# # # # # 2. Implement functions to:
# # # # # -Add new feedback with a specified sentiment.
# # # # # -Display the count of feedback for each sentiment.
# # # # # -Show all feedback messages for a specific sentiment.
# # # # # 3. Utilize built-in dictionary methods to efficiently manage and access the feedback data.
# # # # # 4. Ensure the program handles cases where no feedback is available for a given sentiment.

# # # # # - Intialize your dictionary with empty lists for each sentiment category.
# # # # # -Consider using the 'get()' method for safely retrieving feedback for a sentiment.
# # # # # -Use string methods for standardizing feedback inputs (e.g., converting to lowercase for uniformity).
# # # # # '''
# # # # # def add_feedback(feedback_dict, sentiment, message):
# # # # #     feedback_dict.setdefault(sentiment.lower(), []).append(message)
# # # # #     print(f"Feedback added to '{sentiment}' category.")

# # # # # def display_feedback_count(feedback_dict):
# # # # #     for sentiment, messages in feedback_dict.items():
# # # # #         print(f"{sentiment.title()}: {len(messages)} feedback(s)")

# # # # # customer_feedback = {"postive":  [], "negative": [], "neutral": []}

# # # # # add_feedback(customer_feedback, "Overwhelmingly Postive", "Great product!")

# # # # # print(customer_feedback)

# # # # '''Exercise 6: Inventory Management for a retail store
# # # # Design a program to manage the inventory of products in a retail store. 
# # # # The system should enable updating inventory counts, removing products, and displaying the current inventory status. 

# # # # 1. Use a dictionary to represent the store's inventory, with product names askeys and quantities as values.
# # # # 2. Implement functions for:
# # # # -updating the inventory count for a product. 
# # # # -removing a product from the inventory.
# # # # -displaying the current inventory status.
# # # # 3. Utilize the 'update()' method for adjusting inventory counts and the 'pop()' method for removing products. 
# # # # 4. Ensure error handling for cases liek trying ot remove a non-existent product.

# # # # - Start with pre-populated invetory dictionary. 
# # # # - When updating inventgory, chekc if the product exist before updating its count.
# # # # - Use a lop in th emain program to continuously offer different inventoryh management options.
# # # # '''
# # # # def update_inventory(inventory, product, count):
# # # #     inventory.update({product: count})
# # # #     print(f"Inventory updated: {product} - {count} units.")

# # # # def remove_product(inventory, product):
# # # #     if product in inventory:
# # # #         removed_count  = inventory.pop(product)
# # # #         print(f"Product removed: {product} - {removed_count} units were in stock.")
# # # #     else:
# # # #         print(f"Product '{product}' not found in inventory.")

# # # # def display_inventory(inventory):
# # # #     print("Current Inventory:")
# # # #     for product, count in inventory.items():
# # # #         print(f"{product}: {count} units")

# # # # store_inventory = {"Laptops": 20, "Smartphone": 30, "Headphones": 15}

# # # # update_inventory(store_inventory, "Smartphones", 25)
# # # # remove_product(store_inventory, "Laptops")
# # # # display_inventory(store_inventory)

# # # '''
# # # Exercise 7: Employee Shift
# # # Scheduling system

# # # Create a Python program to manage weekly shift schedule for employees. 
# # # The system should allow copying a week's schedule to another week (both shallow and deep copies), modifying individual

# # # 1. Use a nested dictionary to represent the weekly shift schedules, with outter keys as weeks and inner keys as employee names.
# # # 2. Implement functions for:
# # # - Creating a deep copy of one week's shcedule to another week.
# # # - Creating a shallow copy of one week's schedule ot another week. 
# # # - Displaying the shift schedules for all weeks.
# # # 3. Understand the differences  between shallow and deep copies and their implicaitons on the schedule data.
# # # 4. Handle scenarios such as modifying a shift in a shallow copied week and observing its effect on the original week.

# # # - Intialize the dictianry with a sample schedule for one week.
# # # - Use Python's 'copy' module for deep copying and the dictionary's 'copy'() method for shallow copying.
# # # - Ensure that the deep copy allows independent modifications without affection other weeks. 
# # # '''

# # # import copy

# # # def shallow_copy_schedule(schedules, source_week, target_week):
# # #     schedules[target_week] = schedules[source_week].copy()
# # #     print(f"{target_week}'s schedule copied from {source_week} (Shallow Copy).")

# # # def deep_copy_schedule(schedules, source_week, target_week):
# # #     schedules[target_week] = copy.deepcopy(schedules[source_week])
# # #     print(f"Week  {target_week}'s schedule copied from {source_week} (Deep Copy).")

# # # def modify_shift(schedules, week,employee, shift):
# # #     if week in schedules and employee in schedules[week]:
# # #         schedules[week][employee] = shift
# # #         print(f"Shift updated for {employee} in  {week}:  {shift}.")
# # #     else:
# # #         print(f"Schedule not found for {employee} in {week}.")

# # # def display_schedules(schedules):
# # #     for week, schedule in schedules.items():
# # #         print(f"Week {week}:")
# # #         for employee, shift in schedule.items():
# # #             print(f"{employee}: {shift}")

# # # employee_schedules =  {
# # #     "Week 1": {"Alice": "Morning", "Bob": "Evening", "Charlie": "Night"} 
# # # }

# # # shallow_copy_schedule(employee_schedules, "Week 1", "Week 2")
# # # deep_copy_schedule(employee_schedules,  "Week 1", "Week 3")
# # # modify_shift(employee_schedules, "Week 2", "Alice", "Night")
# # # display_schedules(employee_schedules)


# # '''
# # Exercise 8: Online Course Enrollment System

# # Design a Python program to manage enrollment sfor an online education platform.
# # The system should handle courses, student registrations, and  track which students are enrolled in which courses.

# # 1. Use a nested dictionary structure where the outer dictionary hold courses and each courses and each course key maps to
# # another dictionary of enrolled  students.
# # 2. Implement functions for:
# # - Adding new courses. 
# # - Registering a student for a course
# # - Removing a student from a course.
# # - Displaying all  courses along with their enrolled students.
# # 3. Manage the nested dictianry stgructure to ensure accurate and efficient data handling for course enrollments.

# # Hints:
# # - Start with an empty dictinary for courses and add a few sample courses for testing.
# # - Ensure that students additions and removals correctly update the course's enrollemtn list.
# # - Use loops to iterate through courses and their respective students when displaying the enrollment list.
# # '''

# # def add_course(courses, course_name):
# #     if course_name not in courses:
# #         courses[course_name] = {}
# #         print(f"Course '{course_name}' added successfully.")
# #     else:
# #         print(f"Course '{course_name}' already exists.")

# # def register_student(courses, course_name, student_name):
# #     if course_name in courses:
# #         courses[course_name][student_name] = True #True indicates enrollment
# #         print(f"Student '{student_name}' registered for '{course_name}'.")
# #     else:
# #         print(f"Course '{course_name}' not found.")

# # def remove_student(courses, course_name, student_name):
# #     if course_name in courses and student_name in courses[course_name]:
# #         del courses[course_name][student_name]
# #         print(f"Student '{student_name}' removed from '{course_name}'.")
# #     else:
# #         print(f" Student: or course not found.")

# # def display_enrollments(courses):
# #     for course, students in courses.items():
# #         print(f"Course: {course}")
# #         for student in students:
# #             print(f" Student: {student}")

# # online_courses = {}

# # add_course(online_courses, "Python Programming")
# # add_course(online_courses, "Data Science")
# # register_student(online_courses, "Python Programming", "Alice")
# # register_student(online_courses, "Data Science", "Alice")
# # register_student(online_courses, "Data Science", "Bob")
# # remove_student(online_courses, "Data Science", "Alice")
# # display_enrollments(online_courses)

# '''
# Exercise 9: Health Clinic Patient
# Management System

# Develop a Python program to maintain patient records in a health clinic.
# Each patient record should include personal details and history of visits, with each visit containing date and visit notes.

# 1. Structure the patient records using a dictonary where each patient ID is a key, and the value is another  dictionary containing personal
# details and list of visit record 
# 2. Implement functions for:
# -Adding a new patient with basic details.
# -Recording a new visit for an existing patient.
# -Removing a patient from the system.
# -Displaying a patient's details and visit history.
# 3. Manage the nested structure carefully to ensure data integrity and ease fo access.

# Hints:
# - Initialize with a few patients' data for testing.
# - Use patient ID as a unique identifier for each patient record.
# - Each visit record can be a dictionary within a list, stored in the patient
# 's record'''

# def add_patient(patients, patient_id, name, age):
#     if patient_id not in patients:
#         patients[patient_id] = { "name": name, "age": age, "visits": [] }
#         print(f"Patient '{name}' added with ID '{patient_id}'.")
#     else:
#         print(f"Patient with ID '{patient_id}' already exists.")

# def add_visit(patients, patient_id, date, notes):
#     if patient_id in patients:
#         patients[patient_id]["visits"].append({"date": date, "notes": notes})
#         print(f"Visit on {date} recorded for patient '{patient_id}'.")
#     else:
#         print(f"Patient with ID '{patient_id}' not found.")


# def display_patient_record(patients, patient_id):
#     if patient_id in patients:
#         patient = patients[patient_id]
#         print(f"Patient ID: {patient_id}\\nName: {patient['name']}\nAge: {patient['age']}\nVisits:")
#         for visit in patient['visits']:
#             print(f"  Date: {visit['date']}, Notes: {visit['notes']}")
#     else:
#         print(f"Patient with ID {patient_id} not found.") 

# clinic_patients = {}

# add_patient(clinic_patients, "P001", "Alice Smith", 30)
# add_visit(clinic_patients, "P001", "2022-10-05", "Routine check-up")
# add_visit(clinic_patients, "P001", "2022-10-15", "Follow-up visit")
# display_patient_record(clinic_patients, "P001")

'''
Exercise 10: Real Estate Property
Listing and Insquiry system

Create a Python program for a real estate platform that maintains a list of properties and handles customer inquiries about different properties.

Instructions

1. Use a nested dictionary to prepresent property listings, where each property ID maps to details like location, price, 
and status (available/sold).
2. Implement functions for:
- Adding new property listings.
- Updating the status of a property. 
- Adding customer inquiries for properties.
- Displaying all properties and inquiries made for them.
3. Implement a loop in the main program to allow continuous operation with 
options like adding listings, updating property status, and viewing inquiries.

Hints
-Initialize with a set of sample properties.
-Ensure the program can handle mulitple inquires for the same property.
-Use the property ID as a unique identifier for managing listings.'''

def add_property(properties, property_id, location, price):
    if property_id not in properties:
        properties[property_id] = {"location": location, "price": price, "status": "available", "inquiries": []}
        print(f"Property '{property_id}' added successfully.")
    else:
        print(f"Property ID {property_id} aldready exists.")

def update_status(properties, property_id, status):
    if property_id in properties:
        properties[property_id]["status"] = status
        print(f"Status of property '{property_id}' updated to '{status}'.")
    else:
        print(f"Property ID {property_id} not found.")

def add_inquiry(properties, property_id, customer_name, inquiry):
    if property_id in properties:
        properties[property_id]["inquiries"].append({"customer": customer_name, "inquiry": inquiry})
        print(f"Inquiry added for property '{property_id} by {customer_name}.")
    else:
        print(f"Property ID {property_id} not found.")

def display_properties(properties):
    for pid, details in properties.items():
        print(f"Property ID: {pid}), Location:{details['location']}, Price: {details['price']}, Status: {details['status']}")
    for inquiry in details["inquiries"]:
        print(f"Inquiry by {inquiry['customer']}: {inquiry['inquiry']} ")

real_estate_properties = {}

while True:
    print("\nReal Estate Management System")
    print("1: Add Property\n2: Update Property status\n3: Add Inquiry\n4: Display Properties\n5: Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        pid = input("Enter Property ID: ")
        loc = input("Enter Location: ")
        price = input("Enter Price: ")
        add_property(real_estate_properties, pid, loc, price)
    elif choice == '2':
        pid = input("Enter Property ID: ")
        status = input("Enter new status:(available/sold): ")
        update_status(real_estate_properties,pid,status)
    elif choice == '3':
        pid = input("Enter Property ID: ")
        name = input("Enter Customer Name: ")
        inquiry = input("Enter Inquiry details: ")
        add_inquiry(real_estate_properties, pid, name, inquiry)
    elif choice == '4':
        display_properties(real_estate_properties)
    elif choice == '5':
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")