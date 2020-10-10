import os
from PIL import Image
from pyexiv2 import Image as Image2

def crop360(name):
    image = Image.open(name)
    exif = image.info['exif']
    image_new=Image.new("RGB",(11280,2820),"blue")
    image_new.paste(image,(0,0))
    image_new.paste(image,(5640,0))
    image_new=image_new.crop((2820,0,8460,2820))
    image_new.save(name,'JPEG', exif=exif)

def xmp(name):
    image = Image2(name)
    image.modify_xmp({'Xmp.GPano.ProjectionType': 'equirectangular', 'Xmp.GPano.CroppedAreaImageWidthPixels': '5640', 'Xmp.GPano.CroppedAreaImageHeightPixels': '2820', 'Xmp.GPano.FullPanoWidthPixels': '5640', 'Xmp.GPano.FullPanoHeightPixels': '2820', 'Xmp.GPano.CroppedAreaLeftPixels': '0', 'Xmp.GPano.CroppedAreaTopPixels': '0'})

path = input("Please provide the directory: ")
os.chdir(path)
names = os.listdir('.')

for name in names:
    crop360(name)
    xmp(name)
