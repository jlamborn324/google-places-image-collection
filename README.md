# google-places-image-collection

This repository contains a script to download a user-specified # of satellite images of a given object/place. The use case in this repository is downloading 10,000 satellite images of baseball fields for the purpose of training a neural network. 

# APIs

This script utilizes the Google Places API to find coordinates of locations based on search queries. 

This script utilizes the Mapbox API to download satellite images of given coordinates. 

# Running the Script

There are a couple things that need to be done before you can replicate this code. First, you must add your own API keys for Google Places and Mapbox. **Make sure the API keys work before running the code**

Also, make a folder named 'images' in this directory. This is where the images will be downloaded. 


Once you have added working API keys, run `python3 google-places.py` The script will prompt you to enter a search query and the # of images you wish to download. 

# Problems

The script doesn't work well when a small # of images is requested. This is because I was lazy with the math. To ensure it works, request 40+ images. 

The script can visit the same place multiple times, leading to duplicate images. A feature that tracks places visited and ensures no duplicates are added would be beneficial to the quality of the image data. 
