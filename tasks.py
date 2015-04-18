import json
import urllib2

def getCoordinates(address):
  response = urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=" + address).read()
  response = json.loads(response)
  return [response["results"][0]["geometry"]["location"]["lat"], response["results"][0]["geometry"]["location"]["lng"]]

def getLocationName(lat, lng):
  response = urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + "," + str(lng)).read()
  response = json.loads(response)
  return response["results"][0]["formatted_address"]

def getPointsOfInterest(location):
  response = urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + "," + str(lng)).read()
  response = json.loads(response)
  return response["results"][0]["formatted_address"]  

def findMidpoint(coordinates):
  numCoords = 0.0
  totalX = 0.0
  totalY = 0.0
  Xaverage = 0.0
  Yaverage = 0.0
  isX = True
  for coord in coordinates:
    if(isX == True):
      totalX = totalX + coord
      isX = False
    else:
      totalY = totalY + coord
      isX = True
      numCoords = numCoords + 1
  if(numCoords > 0):
    Xaverage = totalX/numCoords
    Yaverage = totalY/numCoords
  midpoint = [Xaverage, Yaverage]
  return midpoint

getLocationName(-33.9174103,151.2313068)