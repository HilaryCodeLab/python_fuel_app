# Comments are written with a '#' character in the beginning of the line.
# This file will be saved as fuelapp.py
# Create this file in your Desktop
# print('hello world and here is a number', 1+1)
import requests
import feedparser
from pprint import pprint


response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale')
# print(response.content)

feed1 = feedparser.parse(response.content)
entries = feed1['entries']
html_table = '<table><tbody><tr><th>price</th><th>location</th><th>address</th></tr><tr>'
for e in entries:
    print(e['title'])
    html_table = html_table + '<td>' + e['title'].split(':')[0] + '</td><td>' + e['title'].split(':')[1] + '</td><td>' + e['summary']  + '</td></tr>'

html_table = html_table + '</tbody></table>'

f = open('render_table.html', 'w')
f.write(html_table)
f.close()
# my_html_list = ''
# print(feed1)
# pprint(feed1)

# first_name = 'James'
# last_name = 'Bond'

# sentence = 'My name is ' + last_name + ', ' + first_name + ' ' + last_name + '.'
# print(sentence)