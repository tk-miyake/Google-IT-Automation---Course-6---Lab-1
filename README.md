### Introduction

Your company is in the process of updating its website, and they’ve hired a design contractor to create some new icon graphics for the site. 
But the contractor has delivered the final designs in the wrong format -- rotated 90° and too large. 
Oof! You’re not able to get in contact with the designers and your own deadline is approaching fast. 
You’ll need to use Python to get these images ready for launch.

### What you’ll do

Use the Python Imaging Library to do the following to a batch of images:

  - Open an image
  - Rotate an image
  - Resize an image
  - Save an image in a specific format in a separate directory 

### Download the file

Your design contractor sent you the zipped file through his team drive. Download the file from the drive using the following CURL request:

curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie

The images received are in the wrong format:

  - .tiff format
  - Image resolution 192×192 pixel(too large)
  - Rotated 90° anti-clockwise

The images required for the launch should be in this format:

  - .jpeg format
  - Image resolution 128×128 pixel
  - Should be straight

### Write a Python script

This is the challenge section of the lab where you'll write a script that uses PIL to perform the following operations:

  - Iterate through each file in the folder
  - For each file:
      - Rotate the image 90° clockwise
      - Resize the image from 192×192 to 128×128
      - Save the image to a new folder in .jpeg format

Use a nano editor for this purpose. You can name the file however you'd like. And make sure to save the updated images in the folder: /opt/icons/





















