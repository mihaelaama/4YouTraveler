import os   #os module is imported, allowing access to its functions for interacting with the operating system.
import json
import folium
import random
import string
import webbrowser

user_input = str(input('Do you want to travel, but do not know where to go?\n'
                       'From the following list:\n'
                       'Amsterdam, Athens, Barcelona, Belfast, Berlin, Birmingham, Bologna,\n'
                       'Bristol, Brussels, Bucharest, Cambridge, Edinburgh, Liverpool,\n'
                       'London, Madrid, Manchester, Milan, Oslo, Oxford, Paris, Rome,\n'
                       'Vatican, York\n'
                       'Write the name of a city to find out the main attractions: \n'
                       ''))

folder_path = 'tours'
folder_path2 = 'pois'

folder_files1 = os.listdir(folder_path)
folder_files2 = os.listdir(folder_path2)
# os.listdir() is used to retrieve a list of files and directories in the specified directory

data_dict = {}

# Parcurgem fiecare fișier din primul folder
for file1 in folder_files1:
    with open(file1) as f:
        data = json.load(f)
    coord = []
    for item in data:
        coord.append([item['type'], item['name'], item['geoCode']['latitude'], item['geoCode']['longitude']])
    # print(coord)
    # Parcurgem fiecare fișier din al doilea folder
    for file2 in folder_files2:
        # Comparăm numele fișierelor
        if file1[4:] == file2[4:]:
            # Citește conținutul fișierului din al doilea folder
            file2_path = os.path.join(folder_path2, file2)

            with open(file2_path, "r") as file2_handle:
                data2 = json.load(file2_handle)
                # file2_content = file2_handle.read()
                for item2 in data2:
                    coord.append(
                        [item2['subType'], item2['name'], item2['geoCode']['latitude'], item2['geoCode']['longitude'],
                         item2['category']])
    # print(coord)

    data_dict = {file1[5:-5]: coord}
    #print(data_dict)

    oras = user_input
    if oras in data_dict:
        # print(data_dict[oras])
        destinations = []
        coordinates = []
        subTypes = []
        categories = []  # Adăugăm o nouă listă pentru categorii
        categories2 = []
        for element in data_dict[oras]:
            destination = element[1]
            coordinate = element[2:4]
            category = element[4] if len(element) >= 5 else 'TOURS' # Adăugăm categoria în variabila 'category'
            if category not in categories2:
                    categories2.append(category)
            destinations.append(destination)
            coordinates.append(coordinate)
            categories.append(category)  # Adăugăm categoria în lista 'categories'
            #print(categories)
        #print(destinations)
        #print(coordinates)

        category_input = str(input(f'From the folowing category/ies {categories2}, enter the category you are interested in: '))

        filtered_coordinates = [coordinate for coordinate, category in zip(coordinates, categories) if
                                category.lower() == category_input]
        filtered_destinations = [destination for destination, category in zip(destinations, categories) if
                                 category.lower() == category_input]

        folium_map = folium.Map(location=[19.01441, 72.8479385], zoom_start=15, tiles="CartoDB dark_matter")

        counter = 0
        b = 'ABCDEF' + string.digits
        for coordinate, destination in zip(filtered_coordinates, filtered_destinations):
            name = "{0}<br>".format(destination)  #<br> is an HTML tag that represents a line break. It is commonly used
                                                  # in HTML to create a new line or add vertical spacing.
            marker = folium.CircleMarker(location=[coordinate[0], coordinate[1]],
                                         color='#' + ''.join([random.choice(b) for i in range(0, 6)]), popup=name,
                                         fill=True).add_to(folium_map)

        folium_map.location = [coordinate[0], coordinate[1]]
        folium_map.save("final_map.html")

        map_file_path = "final_map.html"
        webbrowser.open_new(map_file_path)
