"""
Python For Everybody

TASK:
sample_data = http://py4e-data.dr-chuck.net/comments_42.xml
expt_data = http://py4e-data.dr-chuck.net/comments_1226900.xml
Return sum of the /count tag present within the /commment tag of the xml file.
"""

# import libraries
import urllib.request
import xml.etree.ElementTree as ET


try:
    # data location
    user_input = input('Enter data location: ')
    response = urllib.request.urlopen(user_input).read()
    print('Retrieving data from', user_input)
    
    # parsing sample_data
    tree = ET.fromstring(response)
    print('Retriving xml tree data...')
    data = tree.findall('comments/comment')
    

    # extract tags data
    sum = 0
    for comment in data:
        count = comment.find('count').text
        sum += int(count)
            
    print(f"Retrieved {len(response)} characters")
    print('Sum of count from all count tags: ',sum)

except:
    print('Enter a valid url for an xml file.')


