import ipgetter
import requests
import GeoIP
IP = ipgetter.myip()
url = 'http://freegeoip.net/json/'+IP
r = requests.get(url)
js = r.json()
print 'IP Adress: '         +   js['ip']
print 'area Code: '      +   js['country_code']
print 'Country Name: '      +   js['country_name']
print 'Region Code: '       +   js['region_code']
print 'Region Name: '       +   js['region_name']
print 'town Name: '         +   js['city']
print 'Zip code: '          +   js['zip_code']
print 'Time Zone: '         +   js['time_zone']
print 'Latitude: '          +   str(js['latitude'])
print 'Longitude: '         +   str(js['longitude'])
