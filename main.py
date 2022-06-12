from hashlib import new
from exif import Image
from geopy.geocoders import Nominatim
import os

def main():
    # ask user to input directory of images
    source_dir = input("Copy and paste the directory in which you want the script to execute in: ")

    with os.scandir(source_dir) as entries:
        for entry in entries:
            file_path = entry.path
            root, file_extension = os.path.splitext(file_path)

            if file_extension != ".jpg" and file_extension != ".png":
                print(f"Skipped {entry.name}. Not an image.")
                continue

            # Read binary of image file and instantiate as exif Image object
            with open(file_path, "rb") as file:
                image = Image(file)

            # if image does not have exif data, skip image (don't rename)
            if not image.has_exif:
                print(f"Skipped {entry.name}. Does not contain exif data.")
                continue

            # extract EXIF data from image
            image_datetime, image_make, image_model, image_gps_lat, image_gps_lat_ref, image_gps_long, image_gps_long_ref = get_exif_data(image)
            
            if image_datetime is None:
                print(f"Skipped {entry.name}. No datetime.")
                continue

            if image_gps_lat is not None:
                # convert GPS coordinates
                latitude, longitude = DMS_to_DD(image_gps_lat, image_gps_lat_ref, image_gps_long, image_gps_long_ref)
                # get address from DD
                road, city, state, country = get_address(latitude, longitude)

            # rename file
            if image_gps_lat is not None:
                new_filename = generate_new_filename(image_datetime, image_make, image_model, road, city, state, country)
            else:
                new_filename = generate_new_filename(image_datetime, image_make, image_model)
            try:
                new_filename += file_extension
                destination = os.path.join(source_dir, new_filename)
                print(f"Converting {entry.name} to {new_filename}")
                os.rename(file_path, destination)
            except: # error handling if there are duplicate image(s)
                print("Duplicate found!")
                new_filename += f" - copy{file_extension}"
                destination = os.path.join(source_dir, new_filename)
                print(f"Converting {entry.name} to {new_filename}")
                os.rename(file_path, destination)


# extract exif data from image and package into list
def get_exif_data(image):
    try:
        image_datetime = image.datetime_original.replace(":","_").replace(" ","_") # TODO: refactor using re.sub()
    except:
        image_datetime = None

    try:
        image_make = image.make
    except:
        image_make = None

    try:
        image_model = image.model
    except:
        image_model = None

    try:
        image_gps_lat = image.gps_latitude
        image_gps_lat_ref = image.gps_latitude_ref
        image_gps_long = image.gps_longitude
        image_gps_long_ref = image.gps_longitude_ref
    except:
        image_gps_lat = None
        image_gps_lat_ref = None
        image_gps_long = None
        image_gps_long_ref = None

    return [image_datetime, image_make, image_model, image_gps_lat, image_gps_lat_ref, image_gps_long, image_gps_long_ref]


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


def generate_new_filename(image_datetime, image_make, image_model, road=None, city=None, state=None, country=None):
    filename = f"{image_datetime}"
    if road is not None:
        filename += f"_{road}_{city}_{state}_{country}"
    if image_make is not None:
        filename += f"_{image_make}"
    if image_model is not None:
        filename += f"_{image_model}"
    return filename


if __name__ == "__main__":
    main()