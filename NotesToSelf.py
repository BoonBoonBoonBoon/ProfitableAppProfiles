from csv import reader

### The Google Play data set ###
opened_file = open('googleplaystore.csv')
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]
android = android[1:]

### The App Store data set ###
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
ios = list(read_file)
ios_header = ios[0]
ios = ios[1:]




# Just takes a header argument and the data, we do this so it can be modular, 
# i.e. instead of passing limited amount of headers we can pass as many as we want.
def imp3_app_data(headers, ios_data):
    
    
    ## Going to need a if statement to check if we have ios data or android data.
    
    # Find column indices for each header
    indices = {header: ios_data[0].index(header) for header in headers}

    # Create a Dictionary that we want to fill with headers and values, that we can return.
    dictapp = {}
    
    #iterate over each row, then use the incdices dictrionry to obtain the row id(name) and assign it.
    for row in ios_data[1:]:
        app_name = row[indices["track_name"]] #object 1 name
        # Make new dict and populate it, 
        # This dictionary comprehension uses the indices dictionary to pull each header and its value from the row, skipping the "track_name" header since it's already used as the main key.
        # app_data holds each header (like "price", "prime_genre", etc.) as a key, with its corresponding data for that row as the value.
        app_data = {header: row[idx] for header, idx in indices.items() if header != "track_name"}
        dictapp[app_name] = app_data

    # Print the dictionary in a readable format
    print("\nApp Data:\n" + "-" * 30)
    for name, data in dictapp.items():
        print(f"App Name: {name}")
        for field, value in data.items():
            print(f"  {field}: {value}")
        print("\n")

    return dictapp


# Usage example:
headers = ["track_name", "price", "prime_genre", "user_rating"]
imp3_app_data(headers, ios)
































# We can use panndas
# print(ios)

# print(ios_header)
print('\n')

# Get the index of the column
#header_Idx_Name = ios_header.index('track_name')
#header_Idx_Price = ios_header.index('price')
#header_Idx_PGenre = ios_header.index('prime_genre')
#header_Idx_Rate = ios_header.index('user_rating')

# Access the column values
#Idx_track_Name = [row[header_Idx_Name] for row in ios]
#Idx_Price = [row[header_Idx_Price] for row in ios]
#Idx_PGenre = [row[header_Idx_PGenre] for row in ios]
#Idx_Rating = [row[header_Idx_Rate] for row in ios]

#app_list = [Idx_Price, Idx_PGenre, Idx_Rating]


# i need to modulize the data, it need to be dynamic,
# as ive hardcoded the, parameters.

# I also need to make it so we have a certain amount of how,
# many we want to print out.
