# 4YouTraveler
API folosit: Amadeus Travel API
Resurse folosite in cadrul API-ului: Destination Experiences APIs:
                                      City search 
                                      Points of Interest (categories: sights, restaurants, nightlife, shopping)
                                      Tours and Activities 
How does the program work?
Doua “programe”:
1) Returnarea coordonatelor (longitudine si latitudine)
City search – “What are the cities matched with keyword ‘user_input‘?
Points of Interest - "What are the best places to visit in user_input?“
Tours and activities - "What are the best tours and activities in this location?"
Obtinem output in format json
Salvam output-ul in fisiere
2) Cream un dictionar cu key = numele orasului, value = destinatiile si informatiile din output
Adaugam informatii points of interest + tours pentru orasele comune
Rafinam dictionarul, pentru a afisa doar destinatiile corespunzatoare orasului introdus ca input de catre utilizator
Afisam destinatiile respective pe harta, cu ajutorul bibliotecii Folium
Cream un pop-up pentru pagina in HTML care reprezinta harta creata (pentru a se deschide automat), cu ajutorul modulului Webbrowser.

Future work
Interfata in HTML conectata cu codul din Python (Python backend), utilizand Flask.
Introducere nume oras + categorie destinatii

References:
https://developers.amadeus.com/self-service/category/destination-experiences
https://github.com/amadeus4dev/amadeus-python
https://github.com/amadeus4dev/amadeus-code examples/blob/master/city_search/v1/get/Python%20SDK/city_search.py
https://github.com/amadeus4dev/amadeus-code-examples
https://github.com/Sandeeppushp/folium-maps
https://www.youtube.com/watch?v=BlETWqnDSnw  
![image](https://github.com/mihaelaama/4YouTraveler/assets/133536193/1c73c94e-ffc6-4ef0-811e-959be1361ff8)




                                      


