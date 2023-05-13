"""
def get_attractions(city):
    #gen_attractions - partea de colectare a datelor
    #apelam api
    #sau citim din fisier dupa city
    return "am gasit atractiile din " + city

while True:
    city = input("Write your city name: ")

    print("\n" + get_attractions(city) + "\n")
"""
"""
import requests
bearer_token = 'qcl1QJdk8z4YOWjnfBPjre19L4wQ'
base_url = 'https://test.api.amadeus.com/v1/reference-data/locations/pois?latitude=41.397158&longitude=2.160873&radius=1&page%5Blimit%5D=10&page%5Boffset%5D=0'
# Define the bearer token
# Set the request headers with the bearer token
headers = {
    'Authorization': f'Bearer {bearer_token}'
}
# Make the GET request with the headers
response = requests.get(base_url, headers=headers)
resp = requests.get(base_url)
data = resp.json()
print(data)
"""

import requests
def get_token():
    import requests

    # Set the request URL
    url = 'https://test.api.amadeus.com/v1/security/oauth2/token'

    # Set the request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Set the request data
    data = {
        'grant_type': 'client_credentials',
        'client_id': 'R81ZUGlbt3iEvGBAGU2A3Jr6C215IpeV',
        'client_secret': 'cRNxjFL5DHyxn0t4'
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=data)

    # Process the response
    if response.status_code == 200:
        # Request was successful
        token_data = response.json()
        # Extract the access token from the response
        access_token = token_data['access_token']
        # Use the access token as needed
    else:
        # Request failed
        print(f'Request failed with status code: {response.status_code}')
        return None
    print(access_token)
    return access_token


def get_api_response():
    bearer_token = get_token()

    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }
    response = requests.get('https://test.api.amadeus.com/v1/reference-data/locations/pois?latitude=41.397158&longitude=2.160873&radius=1&page%5Blimit%5D=10&page%5Boffset%5D=0',
        headers=headers)
    print(response.json())
get_api_response()


from amadeus import Client, ResponseError, Location

amadeus = Client(
    client_id='l27kNTwEGIstw4jrZ029trIAjdDaGjG1',
    client_secret='txRItV7Hs0meVhFY'
)

try:
    try:
        '''
        What are the cities matched with keyword 'Paris' ?
        '''
        response = amadeus.reference_data.locations.cities.get(keyword='Paris')
        print(response.data)
        response = amadeus.shopping.activities.get(latitude=48.85341, longitude=2.3488)
        print(response.data)
    except ResponseError as error:
        raise error
except ResponseError as error:
    print(error)

