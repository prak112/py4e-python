"""
Python For Everybody

TASK:
Return sum of the /count tag present within the /commment tag of the xml file.
"""

# import libraries
import urllib.request
import xml.etree.ElementTree as ET

# data-location
sample_url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
expt_url = 'http://py4e-data.dr-chuck.net/comments_1226900.xml'

# parsing sample_data and counting
response = urllib.request.urlopen(sample_url).read()
tree = ET.fromstring(response)
data = tree.findall('comments/comment')

sum = 0
for comment in data:
    sum += int(comment.find('count').text)
print(sum)