"""
Python For Everybody

TASK:
sample_data = http://py4e-data.dr-chuck.net/comments_42.json
expt_data = http://py4e-data.dr-chuck.net/comments_1226901.json
Return sum of the /count tag present within the /commment tag of the xml file.
"""

# import libraries
import urllib.request
import json

try:
    # locate & load data
    user_input = input('Enter URL: ')
    print('Retrieving data from', user_input)
    response = urllib.request.urlopen(user_input)
    data = json.load(response)
    print('Keys of loaded json dictionary: ', data.keys())
    
    # extract count values
    count_sum = []
    for ele in range(len(data['comments'])):
        count_sum.append(data['comments'][ele]['count'])
    print('Total Count keys:', len(count_sum))
    print('Sum of Count values:', sum(count_sum))
except:
    print('Enter a valid URL.')