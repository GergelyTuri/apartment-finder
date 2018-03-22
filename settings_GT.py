import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 1750

# The maximum rent you want to pay per month.
MAX_PRICE = 2250

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'newyork'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["mnh"]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "wash_heights_west": [
        [-73.963777, 40.81781],
        [-73.935841, 40.850097]
    ],
    "wash_heights_inwood": [
        [-73.942656,40.845264],
        [-73.909525,40.878131]
    ],
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["morningside", "inwood", "wash hts", "washington heights", "Inwood / Wash Hts"]

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 3 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "one_191" : [40.8553621, -73.9295207],
    "one_215" : [40.8696056, -73.9153168],
    "one_181" : [40.8491196, -73.9337381],
    "A_181" : [40.8507855, -73.9384604],
    "A_Dyckman" : [40.8652172, -73.9272555],
    "A_207" : [40.8678989, -73.9212342],
    "M98_w178": [40.8482027, -73.9373580],
    "M98_w181": [40.8511608, -73.9380835],
    "M98_w183": [40.8523979, -73.9376530],
    "M98_w185": [40.8536380, -73.9372627],
    "M98_w187": [40.8550718, -73.9367223],
    "M98_w190": [40.8573338, -73.9353329],
    "M98_cabrini": [40.8590130, -73.9342500]
}

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'aap'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#housing"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "xoxp-317843647830-318046892823-329668335654-35c43b8210372069c631e756877f50a0")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass