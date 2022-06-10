from exif import Image
from geopy.geocoders import Nominatim

def main():
    # ask user to input directory of images
    #file_path = input("Copy and paste the directory in which you want the script to execute in: ")
    file_path = "20160712_174018.jpg" # test only

    # Read binary of image file and instantiate as exif Image object
    with open(file_path, "rb") as file:
        image = Image(file)

    # if image does not have exif data, skip image (don't rename)
    #if not image.has_exif:
        #continue

    # extract EXIF data from image
    image_datetime, image_make, image_model, image_gps_lat, image_gps_lat_ref, image_gps_long, image_gps_long_ref = get_exif_data(image)

    # convert GPS coordinates
    latitude, longitude = DMS_to_DD(image_gps_lat, image_gps_lat_ref, image_gps_long, image_gps_long_ref)

    # get address from DD
    road, city, state, country = get_address(latitude, longitude)

    # rename file
    print(f"{image_datetime}_{road}_{city}_{state}_{country}_{image_make}_{image_model}")


# extract exif data from image and package into list
def get_exif_data(image):
    image_datetime = image.datetime_original.replace(":","_").replace(" ","_") # TODO: refactor using re.sub()
    return [image_datetime, image.make, image.model, image.gps_latitude, image.gps_latitude_ref, image.gps_longitude, image.gps_longitude_ref]


# convert GPS coord from DMS (Degree, Minutes, Seconds) to DD (Decimal Degrees)
def DMS_to_DD(latitude_DMS, latitude_ref, longitude_DMS, longitude_ref):
    # Convert latitude
    d, m, s = latitude_DMS
    latitude_DD = (d + m / 60.0 + s / 3600.0) * (1 if latitude_ref == "N" else -1)
    
    # Convert longitude
    d, m, s = longitude_DMS
    longitude_DD = (d + m / 60.0 + s / 3600.0) * (-1 if longitude_ref == "W" else 1)

    return [latitude_DD, longitude_DD]


# given latitude and longitude in DD, return road, city, state, and country
def get_address(latitude, longitude):
    coord_decimal = f"{latitude}, {longitude}"
    geolocator = Nominatim(user_agent="http")
    location = geolocator.reverse(coord_decimal)

    road = location.raw.get('address').get('road').replace(" ", "")
    city = location.raw.get('address').get('city').replace(" ", "")
    state = location.raw.get('address').get('state').replace(" ", "")
    country = location.raw.get('address').get('country').replace(" ", "")
    return [road, city, state, country]


if __name__ == "__main__":
    main()