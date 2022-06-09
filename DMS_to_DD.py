# Converts GPS Coordinates from Decimal Minutes Seconds (DMS) to Decimal Degrees (DD)

gps_latitude = "(29.0, 42.0, 12.0)"
gps_latitude_ref = "N"
gps_longitude = "(95.0, 33.0, 13.0)"
gps_longitude_ref = "W"

# Remove parenthesis
gps_latitude = gps_latitude.replace('(','')
gps_latitude = gps_latitude.replace(')','')
gps_longitude = gps_longitude.replace('(','')
gps_longitude = gps_longitude.replace(')','')

# Convert latitude
d, m, s = [float(item.strip()) for item in gps_latitude.split(',')]
latitude = (d + m / 60.0 + s / 3600.0) * (1 if gps_latitude_ref == "N" else -1)

# Convert longitude
d, m, s = [float(item.strip()) for item in gps_longitude.split(',')]
longitude = (d + m / 60.0 + s / 3600.0) * (-1 if gps_longitude_ref == "W" else 1)


print(latitude, longitude)