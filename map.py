
import folium
import random
import string

folium_map = folium.Map(location=[19.01441, 72.8479385],
                        zoom_start=5,
                        tiles="openstreetmap")
# CartoDB dark_matter
# openstreetmap
# stamenterrain
# stamentoner
# stamenwatercolor
# cartodbpositron


cities=['balotra', 'bengaluru', 'hyderabad', 'lachhmangarh', 'meerut', 'new delhi', 'ahmedabad', 'albuquerque', 'apache junction', 'avondale', 'bisbee', 'bouse', 'bullhead city', 'carefree', 'chandigarh', 'delhi', 'farmington', 'greater noida', 'gurgaon', 'indore', 'las cruces', 'mumbai', 'noida', 'pune', 'rio rancho', 'roswell', 'santa fe', 'agra', 'faridabad', 'abu zabi', 'ahorn', 'ajman', 'al-fujayrah', 'allershausen', 'attenhofen', 'bad birnbach', 'bad endorf', 'bad gronenbach', 'chennai', 'dubai', 'edison', 'elizabeth', 'jersey city', 'kolkata', 'newark', 'paterson', 'ras al-khaymah', 'sharjah', 'umm al qaywayn', 'woodbridge', 'ghaziabad', 'afzalpur', 'akalkot', 'ambada', 'boston', 'gazipur', 'jaipur hat', 'los angeles', 'miramar', 'new york', 'surat', 'airmont', 'ajmer', 'albany', 'alden', 'ambert', 'amherst', 'amityville', 'amsterdam', 'banswara', 'burhanuddin', 'creuzier-le-vieux', 'ferrieres', 'komilla', 'legaspi', 'lerdo', 'maafushi', 'monaco-ville', 'nalitabari', 'pasir mas', 'peschadoires', 'riotord', 'saint-pal-de-chalencon', 'tungi', 'achampudur', 'acworth', 'adel', 'adityapur', 'adoni', 'ahmednagar', 'akividu', 'akron', 'aligarh', 'allahabad', 'alledonia', 'alliance', 'alma', 'alpharetta', 'alwar', 'amalapuram', 'ambala', 'americus', 'anakapalle', 'apple creek', 'archbold', 'asifabad', 'bagalkot', 'bellary', 'bhilwara', 'bhopal', 'bilari', 'daman', 'diu', 'faizabad', 'fatehgarh', 'habra', 'haridwar', 'hubli', 'islampur', 'jabalpur', 'jamshedpur', 'kalol', 'kenmore', 'kochi', 'korba', 'kota', 'latur', 'mangalore', 'mango', 'morbi', 'panvel', 'raipur', 'rajgamar', 'rurki cantonment', 'satna', 'sikkim', 'silvassa', 'udaipur', 'visapur', 'anthiyur', 'asansol', 'barkot', 'belur', 'darjiling', 'dehradun', 'durgapur', 'gaya', 'haldwani', 'howrah', 'jhansi', 'kanpur', 'karnal', 'kedarnath', 'kotdwara', 'lucknow', 'mathura', 'nainital', 'navi mumbai', 'panipat', 'patna', 'ranipur', 'rohtak', 'roorkee', 'rudraprayag', 'siliguri', 'sonipat', 'sultanpur', 'vadodara', 'varanasi', 'alore', 'adelanto', 'agoura hills', 'aguanga', 'akonolinga', 'amman', 'aurangabad', 'bafia', 'brooks', 'brussel', 'eseka', 'hapur', 'henderson', 'khatauli', 'malton', 'mbalmayo', 'mfou', 'monatele', 'nagpur', 'nashik', 'oriximina', 'paris', 'scottish borders', 'south wales', 'south yorkshire', 'abensberg', 'abingdon', 'aichach', 'ainring', 'alexandria', 'altdorf', 'altotting', 'altusried', 'ashburn', 'ashland', 'aylett', 'abbin', 'adari', 'addanki', 'akola', 'al-""aqabah', 'al-quwayrah', 'amroli', 'anjarah', 'arjan', 'ashokpuram', 'attleborough', 'ayn janna', 'bacton', 'bahadurganj', 'bandora', 'barauli', 'bath', 'bhosari', 'briston', 'chakan', 'daet', 'dereham', 'deuba', 'diss', 'downham market', 'dyer', 'eshkashem', 'fakenham', 'garboldisham', 'gayton', 'great yarmouth', 'halawah', 'heacham', 'iriga', 'itanagar', 'kings lynn', 'kolhapur', 'kufranjah', 'kyoto', 'little cressingham', 'luxembourg', 'macau', 'male', 'manila', 'mirzapur', 'naga', 'navi mumbai panvel', 'pune cantonment', 'solapur', 'sorsogon', 'vellore', 'secunderabad', 'anchorage', 'bampton', 'banbury', 'barrow', 'bethel', 'bicester', 'blewbury', 'cheltenham', 'chipping norton', 'college', 'fairbanks', 'homer', 'aalen', 'aberdeen', 'achern', 'aichtal', 'airway heights', 'albstadt', 'alderwood manor', 'aldingen', 'allmersbach', 'anacortes', 'arlington', 'auburn', 'detroit', 'modinagar', 'san francisco', 'alta loma', 'ar-riyad', 'bundi', 'churu', 'clifton park', 'hakkari', 'halawa', 'jaipur', 'jaisalmer', 'jodhpur', 'london', 'new ', 'schofield barracks', 'shanghai', 'ulsan', 'abidjan', 'ankara', 'baghdad', 'bangkok', 'barcelona', 'belo', 'bogota', 'buenos', 'cairo', 'chicago', 'dallas', 'dar', 'dhaka', 'dongguan', 'fortaleza', 'guangzhou', 'harbin', 'hong', 'houston', 'ho', 'istanbul', 'jeddah', 'johannesburg', 'kabul', 'khartoum', 'kinshasa', 'kitakyushu', 'kuala', 'lima', 'los', 'luanda', 'madrid', 'medellin', 'melbourme', 'mexico', 'miami', 'monterrey', 'montréal', 'nagoya', 'nairobi', 'nanjing', 'new', 'osaka', 'quingdao', 'riyadh', 'santiago', 'shantou', 'singapore', 'sydney', 'tehran', 'tianjin', 'toronto', 'washington', 'wuhan', 'xian', 'yangon', 'zhengzhou']
dataa=[[25.834763, 72.2410908], [12.9791198, 77.5912997], [25.3801017, 68.3750376], [27.3637739, 76.8581926], [28.9963296, 77.7061915], [28.6141793, 77.2022662], [23.0216238, 72.5797068], [35.0841034, -106.6509851], [33.4150484, -111.5495439], [33.4354989, -112.3495572], [31.4481481, -109.9284025], [33.9352235, -114.0294032], [35.1358413, -114.5287143], [33.8222752, -111.9175949], [30.7194022, 76.7646552], [28.6517178, 77.2219388], [36.729067, -108.2054644], [28.4670734, 77.5137649], [28.4646148, 77.0299194], [22.7203616, 75.8681996], [32.3140354, -106.7798078], [18.9387711, 72.8353355], [28.5726442, 77.3547609], [18.521428, 73.8544541], [35.233375, -106.6644716], [33.3943282, -104.5229518], [-31.6186951, -60.7019561], [27.1752554, 78.0098161], [28.402837, 77.3085626], [24.3964744, 54.5366631], [48.1629262, 11.5791979], [25.4037872, 55.5262841], [23.28, 57.97], [48.433305, 11.5999989], [48.6498061, 11.8477731], [48.4431424, 13.0893817], [47.906411, 12.3013697], [47.8774446, 10.2217265], [13.0801721, 80.2838331], [25.0750095, 55.1887609], [40.5382375, -74.3945173], [40.6639916, -74.2107006], [40.7281575, -74.0776417], [22.5677459, 88.3476023], [40.735657, -74.1723667], [40.9167654, -74.171811], [25.7737705, 55.938232], [24.0002488, 53.9994829], [25.5685229, 55.6496719], [52.0940952, 1.3201301], [28.711241, 77.4445372], [17.2005764, 76.3605783], [17.4507852, 76.1385307], [20.9063194, 77.520082], [42.3602534, -71.0582912], [23.9980797, 90.4229848], [25.1027403, 89.0259568], [34.0536909, -118.2427666], [25.9759115, -80.3347213], [40.7127281, -74.0060152], [21.1864607, 72.8081281], [41.1009293, -74.1162544], [26.4691, 74.639], [42.6511674, -73.754968], [42.4589075, -88.5178757], [45.5504338, 3.742639], [42.3803676, -72.523143], [40.6721763, -73.414846], [52.3745403, 4.8979755], [23.5, 74.333333], [22.5012535, 90.7293339], [46.1593352, 3.4382924], [43.0109218, -0.2629307], [23.4610615, 91.1808748], [9.7091058, 123.3371787], [35.4902351, -119.1526049], [3.9411571, 73.489928], [43.7309697, 7.4248152], [25.0896639, 90.194301], [6.0080942, 102.0925134], [45.8250592, 3.4925107], [45.2319771, 4.4010859], [45.3564714, 3.9563812], [-6.8352543, 39.327323]]

counter=0
b='ABCDEF'+string.digits
for i in dataa:
        namee=cities[counter]
        name = "City: {0}<br>".format(namee)

        marker = folium.CircleMarker(location=[i[0],i[1]],color='#'+''.join([random.choice(b) for i in range(0,6)]),popup=name,fill=True).add_to(folium_map)
        counter=counter+1


folium_map.save("my_map.html")

"""
some_dict = {1: 'one', 2: 'two', 3: 'three'}
list_of_keys = list(some_dict.keys())
print(list_of_keys) # [1, 2, 3]
"""

