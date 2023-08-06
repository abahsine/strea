from exif import Image
img_filename = 'monument.jpg'
with open(img_filename, 'rb') as img_file:
    img = Image(img_file)

print(img.get("gps_latitude"),img.get("gps_longitude"))
my_north = (47,13,42.666)
my_east = (5,58, 48.575)

img.gps_latitude = my_north
img.gps_longitude = my_east


with open(f'{img_filename}', 'wb') as image_save:
    image_save.write(img.get_file())


