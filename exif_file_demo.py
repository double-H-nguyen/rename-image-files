from exif import Image

file_path = "20160712_174018.jpg"

# Read binary of image file
with open (file_path, "rb") as file1:
    image1 = Image(file1) # instantiate exif Image object

if image1.has_exif:
    print(f"This image contains EXIF (version {image1.exif_version}) information.") 
    print("-------------------------------------")
    tags = dir(image1) # expose EXIF tags
    print(f"List of available EXIF tags in this image:")
    for tag in tags:
        print(tag)
    print("-------------------------------------")
    print(f"make: {image1.make}")
    print(f"model: {image1.model}")
    print(f"datetime: {image1.datetime}")
    print(f"datetime_original: {image1.datetime_original}")
    print(f"resolution: {image1.pixel_x_dimension}x{image1.pixel_y_dimension}")
    print(f"Raw GPS coords: {image1.gps_latitude}{image1.gps_latitude_ref} {image1.gps_longitude}{image1.gps_longitude_ref}")
else:
    print("This image does not contain any EXIF information.")
    print("-------------------------------------")