from math import radians, cos, sin, asin, sqrt
from twilio.rest import TwilioRestClient

def distance(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    print(km)
    return km

def distanceWrapper(item, userlat, userlng):
    return distance(item.item_longitude, item.item_latitude, float(userlng), float(userlat))

def sendMessage(msg,number):
    # put your own credentials here
    ACCOUNT_SID = 'ACf707ea7d265d7bd6b1f038c71639168e'
    AUTH_TOKEN = '23f2f33f29c6da0d54922db9079965c6'

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    number = '0425864138'

    print('Sending message to ' + number)
    client.messages.create(
        to = number,
        from_ = '+61428954627',
        body = msg,
    )
