#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join, splitext
from fractions import Fraction
import math
import sys

try:
	from PIL import Image
except ImportError:
	sys.exit("You need Pillow!\ninstall it from https://pillow.readthedocs.io/en/3.3.x/installation.html#basic-installation")

version = 0.1

## CONFIG

# Paths to folders
paths = {
	'images' : '../images',
	'sponsors' :'../sponsors',
	'event_graphics' : '../aaulan_graphics',
	'output' : '../output',
}

allowed_file_extensions = ['.png', '.jpg', '.jpeg']

# Overlay sizes as fraction of image dimensions (0.0 to 1.0)
size_scalars = {
	'event_graphics' : [1, 0.15],
	'sponsor_box' : [0.8, 0.25],
}

# Overlay offsets as fraction of image dimensions (0.0 to 1.0)
offset_scalars = {
	'event_graphics' : [0.15, 0.1], # This has origin top left
	'sponsor_box' : [0, 0.1], # This has origin bottom center
}

# Sponsor rotations in degrees CW
rotations = {
	'sponsor' : 30
}

## END OF CONFIG

# TODO Unfinished function
def get_images(path, file_types):
	"This returns a list of all images of allowed type in the path"
	#print("Getting images from {} of type {}".format(path, ','.join(file_types)))
	print("Getting images from {}".format(path))

	# List all files and remove files that aren't images from the list
	images = [f for f in listdir(path) if isfile(join(path, f))]

	for item in images:
		file_name, ext = splitext(item)
		if ext.lower() not in [x.lower() for x in file_types]:
			images.remove(item)

	return images

# TODO Unfinished function
def generate_sponsor_overlay(path, file_types, offset, size, rotation):
	print("nah")
	# Get all sponsor overlays
	
	# Rotate them rotation_degrees

	# Get max size of all logos

	# Resize and distribute all images to fit

	# Add "Powered by:" text

	# Offset sponsor overlay

	# Return image consisting of sponsor overlay

# TODO Unfinished function
def generate_event_overlay(path, file_types, offset, size, season):
	print("eeh")
	# Get all event overlays

	# Pick appropriate files depending on season

	# Resize and distribute all images to fit

	# Offset 

	# Return image

# TODO Unfinished function
def apply_overlay(image, file_types):
	
	background = Image.open(image)

	# We assume the image is the wanted size of our output images
	image_width, image_height = background.size
	ratio_overlay = Fraction(ResizeWidth, ResizeHeight) # Currently unused

	# Handle portrait images in this if
	if image_width < image_height:
		warn("Portrait images currently not supported")
		return

	# Get size of image, 
	# calculate sizes for different overlay elements

	# Get sponsor overlay and apply

	# Get event overlay and apply

	# Return finished image



# TODO Unfinished
for img in get_images(paths['images'] , allowed_file_extensions):
	print("meh")
	# For each image, apply an overlay, and save the returned output

	# output = apply_overlay(img, allowed_file_extensions)

	#output.save(paths['output'] + "/" + output)
	# background.close()