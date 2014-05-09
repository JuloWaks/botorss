#/usr/bin/env python

import requests
import datetime
import sys
import xml.etree.ElementTree as ET
__author__ = 'JuloWaks'


def GetXml(url):
    local_fname = url.split('/')[2] # Getting the most probably name of the website ['http://','','www.foo.com']
    local_fname += str(datetime.datetime.utcnow()) # OR datetime.datetime.today().date() when does once a day

    r = requests.get(url, stream=True) # if stream=true prevent getting out of memory
    with open(local_fname,'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return local_fname



if len(sys.argv) != 2: # Validation
    print('To use Botorss just write \"python botorss.py \'http://thesite.com/rss\' ')
    exit()

url = sys.argv[1].lower()
xml = GetXml(url)

tree = ET.parse(xml)
root = tree.getroot()

for channel in root.findall('channel'): # Do this in case there is more than 1 channel in the rss

    print (channel.find('title').text) # Reference to the channel title

    for item in channel.findall('item'): # In almost every case has this format
        title = item.find('title').text
        print ( title +' : ' + str(len(title)))












