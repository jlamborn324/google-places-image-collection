import urllib.request
import json
import csv

# Thanks to https://simplemaps.com/data/us-cities for the .csv of U.S. cities

# MAPBOX_API_KEY = ""  # INSERT YOUR API KEYS HERE
# GOOGLE_API_KEY = ""  # INSERT YOUR API KEYS HERE

MAPBOX_API_KEY = ""
GOOGLE_API_KEY = ""


data_path = "preparsed-data.json"  # Location where each .json from the Places API will be downloaded. This will be replaced every time a new json is downloaded from
# the Places API.

mapbox_template = "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/{y},{x},{z},0/400x400@2x?access_token={key}"

global_counter = (
    0  # Used to keep track of # of images downloaded, also used to name the images
)


google_template = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&location={lat},{long}&radius={radius}&key={key}"

# url = google_template.format(query='Baseball%20Fields', lat='38.8892', long='-77.05', radius='500', key=GOOGLE_API_KEY)


"""
Function that takes in a latitude and longitude, and radius (in meters), and returns a list of coordinates 
for the 20 closest baseball fields. Uses Google Places API
"""


def coordsGrabber(query: str, lat: str, long: str, radius: str):

    url = google_template.format(
        query=query,
        lat=lat,
        long=long,
        radius=radius,
        key=GOOGLE_API_KEY,  # Constructs the URL for the API request
    )

    urllib.request.urlretrieve(url, data_path)

    coords = []
    with open(data_path) as f:
        data = json.load(f)

    for i in data["results"]:
        coords.append([i["geometry"]["location"], i["formatted_address"]])
        # print(i['formatted_address'])

    return coords


# coords = (coordsGrabber("Baseball%20Fields", '38.8892', '-77.05', '40000'))

"""
Function that takes in a set of coordinates and a zoom level 
and returns a satellite image at that location. Powered by Mapbox API
"""


def imageGrabber(zoom, field_coords):

    global global_counter

    for coordinate in field_coords:
        url = mapbox_template.format(
            x=str(coordinate[0]["lat"]),
            y=str(coordinate[0]["lng"]),
            z=zoom,
            key=MAPBOX_API_KEY,
        )
        urllib.request.urlretrieve(
            url, "images/" + str(global_counter) + ".jpg"
        )  # Image is named based on the global_counter so every image has different name
        print("Downloading image # " + str(global_counter))
        global_counter += (
            1  # Counter increases by one for every satellite image that is downloaded
        )


"""
Function that uses coordsGrabber to select coordinates, and imageGrabber to download satellite images at those coordinates. 
This function uses a .csv of U.S. cities in the United States to spread the API requests over a diverse area. 
"""


def driver(url, num_of_pictures, query):

    num_of_cities = 28500  # number of cities in uscities.csv

    num_of_requests = (
        num_of_pictures / 20
    )  #  Holds the number of google places API requests needed to reach the # of pictures wanted
    # 20 places given per each Places API request, so the number of pictures needed/ 20 = number of requests needed
    city_interval = (
        num_of_cities / num_of_requests
    )  # city_interval determines how many cities the program will skip during each iteration.
    # For example, we may want to cover only every 50th city in the list to ensure that we are covering all of the U.S. The .CSV is ordered by state

    counter = (
        0  # this counter is used to keep track of which line of the .csv the loop is on
    )
    cities_searched = 0  # keeps track of # of cities that have been searched

    with open(url) as file:
        readcsv = csv.reader(file, delimiter=",")
        file.readline()  # get rid of that pesky first line

        for row in readcsv:  # 8th index is lat 9th index is long
            counter += 1

            # if cities_searched == 3: exit(1)    # Counter for testing few iterations
            if counter % city_interval == 0:  # If we've reached a city interval
                tuple(row)

                field_coords = coordsGrabber(
                    query, row[8], row[9], 50
                )  # Call the coordsGrabber with the search string "Baseball Fields" and a radius of 50
                imageGrabber(17, field_coords)

                cities_searched += 1

            else:
                continue


query = input(
    "Please enter your search query for satellite images (Example: Baseball fields): "
)
query = query.replace(" ", "%20")

print(query)

pics = input("Please enter the # of images you would like to download: ")

if pics != input("Please reenter the # of images you would like to download: "):
    print("These requests do not match")
    exit(1)

driver("uscities.csv", int(pics), query)
