"""
Python For Everybody

TASK:
Prompt for a location, contact a web service and retrieve JSON for the web service and parse that data.
Retrieve the first place_id from the JSON. 
A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

sample = South Federal University
expt = Universidad de Buenos Aires
"""

# import libraries
import urllib.parse, urllib.request
import json

try:
    # location to retrieve
    user_input = input('Enter Location: ')

    # api details
    api_key = 42
    api_url = 'http://py4e-data.dr-chuck.net/json?'
    params = {'address': user_input, 'key' : api_key}
    url = api_url + urllib.parse.urlencode(params) # combining api call and encode parameters into url

    # call api & retrieve place_id
    url_h = urllib.request.urlopen(url)
    print('Calling API...')
    data = url_h.read().decode()
    json_data = json.loads(data)
    print('Retrieving data...')
    if json_data is None:
        print('-x-x-x-x---Failed to Retrieve data---x-x-x-x-')
    else:
        print('Identifying keys..\n',json_data.keys())
        #print('\n',json.dumps(json_data, indent=4)) # view json_data with indentations
        print('Retrieved Characters: ', len(json.dumps(json_data)))
        print('Place-Id: ', json_data['results'][0]['place_id'])

except:
    print('Enter a valid Location.')