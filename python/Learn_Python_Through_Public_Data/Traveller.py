#!/usr/bin/env python

# Imports first

import urllib
from xml.etree.ElementTree import parse

u = urllib.urlopen('http://www.ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()

doc = parse('rt22.xml')
wanted_ones = [ ]
for bus in doc.findall('bus'):
    direction = 'South' in bus.findtext('d')
    bus_id = bus.findtext('id')[0] == '1'
    if bus_id and direction:
        wanted_ones.append(bus)

lons = [float(i.findtext('lon')) for i in wanted_ones]
print 'The Buses that may have the suitcase are', str(len(wanted_ones))
print 'longitude of the buses: ',lons
