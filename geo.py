from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Andre")
location = geolocator.geocode("Los naranjos tlaquepaque")
print(location.address)

print((location.latitude, location.longitude))

lat = location.latitude
