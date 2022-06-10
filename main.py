from exif import Image

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

    # convert GPS coord from DMS to DD

    # get address from DD

    # rename file


# extract exif data from image and package into list
def get_exif_data(image):
    image_datetime = image.datetime_original.replace(":","_").replace(" ","_") # TODO: refactor using re.sub()
    return [image_datetime, image.make, image.model, image.gps_latitude, image.gps_latitude_ref, image.gps_longitude, image.gps_longitude_ref]


if __name__ == "__main__":
    main()