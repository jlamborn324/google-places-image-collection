# google-places-image-collection

This repository contains a script to download a user-specified # of satellite images of a given object/place. The use case in this repository is downloading 10,000 satellite images of baseball fields for the purpose of training a neural network. 

# APIs

This script utilizes the Google Places API to find coordinates of locations based on search queries. 

This script utilizes the Mapbox API to download satellite images of given coordinates. 

# Running the Script

There are a couple things that need to be done before you can replicate this code. First, you must add your own API keys for Google Places and Mapbox. **Make sure the API keys work before running the code**

If you wish to recieve images of something other than baseball fields, you must change "Baseball%20Fields" in line 118 to your preferred search string. **Be sure to add %20 instead of spaces.** 

You can also customize the # of images you wish to download. In line 128, change '10000' to the number of images you wish to download. 

Once you have made these changes, run `python3 google-places.py` The script will begin to populate a folder named images with satellite images of places found from your search query. 
