import json

user_input = str(input('Write the name of the city: \n'
                       ''))
from amadeus import Client, ResponseError, Location

amadeus = Client(
    client_id='R81ZUGlbt3iEvGBAGU2A3Jr6C215IpeV',
    client_secret='cRNxjFL5DHyxn0t4'
)

try:
    try:
        '''
        What are the cities matched with keyword ' ' ?
        '''
        response = amadeus.reference_data.locations.cities.get(keyword=user_input)
        #print(response.data)

        file_path = 'output.json'
        with open (file_path, 'w') as file:
            json.dump(response.data, file)

        #print(f"Output saved to {file_path}")
        #response = amadeus.shopping.activities.get(latitude=48.85341, longitude=2.3488)
        #print(response.data)
    except ResponseError as error:
        raise error
except ResponseError as error:
    print(error)

import json
jsonFile = 'output.json'
with open(jsonFile, 'r') as file:
    data = json.load(file)
city_name = data[0]['name']
latitude = data[0]['geoCode']['latitude']
longitude = data[0]['geoCode']['longitude']

#print(f"City Name: {city_name}")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

try:
    try:
        #What are the popular places in ' ' (based on the geo location)
        response = amadeus.reference_data.locations.points_of_interest.get(latitude=latitude, longitude=longitude)
        response2 = amadeus.shopping.activities.get(latitude=latitude, longitude=longitude)
        #response3 = amadeus.reference_data.locations.airports.get(latitude=latitude, longitude=longitude)
        print(response.data, "----------------------------------------------------------------------------------------")
        #print(response2.data, "----------------------------------------------------------------------------------------")
        #print(response3.data, "-----------------------------------------------------------------------------------------")

        file_path2 = 'output_final6.json'
        with open(file_path2, 'w') as file:
            json.dump(response.data, file)
    except ResponseError as error:
        raise error
except ResponseError as error:
    raise error

"""
jsonFile2 = 'output_final6.json'
with open(jsonFile2, 'r') as file:
    data2 = json.load(file)
    
# create an empty list to store the 'name' values
names = []

# iterate over each element in the data2 list and append the 'name' value to the names list

for element in data2:
    name = element['name']
    names.append(name)

# print out the names list
print(f"Point of interest: {names}")
"""
