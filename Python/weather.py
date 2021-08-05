#JSON JavaScript Object Notation

import json

def k2f(k):
    f=str(round((k-273.15)*1.8+32,1))+'F'
    return f

w= json.loads('{"coord":{"lon":-78.4942,"lat":42.0901},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"base":"stations","main":{"temp":280.01,"feels_like":280.01,"temp_min":279.15,"temp_max":281.15,"pressure":1013,"humidity":49},"visibility":10000,"wind":{"speed":0.07,"deg":357,"gust":0.39},"clouds":{"all":75},"dt":1618450712,"sys":{"type":1,"id":5202,"country":"US","sunrise":1618396461,"sunset":1618444413},"timezone":-14400,"id":5106994,"name":"Allegany","cod":200}')


print('Current weather in %s:' % (w['name']))
print('Current Temp: ' + k2f(w['main']['temp']))
print('Weather: ' + w['weather'][0]['main']+ ' - ' +w['weather'][0]['description'])
print('High: ' + k2f(w['main']['temp_max']))
print('Low: ' + k2f(w['main']['temp_min']))
print('Humidity: ' + str(w['main']['humidity'])+'%')

