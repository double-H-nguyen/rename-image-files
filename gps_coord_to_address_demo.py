from geopy.geocoders import Nominatim

coord_decimal = "29.7033333,-95.55361111111111"

geolocator = Nominatim(user_agent="http")
location = geolocator.reverse(coord_decimal)
print(f"Raw JSON: \n {location.raw}")
print(f"Address: {location.address}")
print(f"Road: {location.raw.get('address').get('road')}")
print(f"City: {location.raw.get('address').get('city')}")
print(f"State: {location.raw.get('address').get('state')}")
print(f"Country: {location.raw.get('address').get('country')}")