'''
Author: Sumanth Paranjape
Version: 1.0
Function: Parses exoplanet data and displays information according to requirements.
Libraies: urllib, json
'''
import urllib, json
import urllib.request as urlRequest
import traceback

''' 
If fields HostStarMassSlrMass, HostStarRadiusSlrRad, 
HostStarMetallicity, HostStarTempK, HostStarAgeGyr are empty
it means the planet probably does not have a star.
Returns the count of all such tuples.
'''
def number_of_planets_without_stars(data):
    count = 0
    for i in range(0, len(data)):
        if not data[i]["HostStarMassSlrMass"] and not data[i]["HostStarRadiusSlrRad"] and \
        not data[i]["HostStarMetallicity"] and not data[i]["HostStarTempK"] and \
        not data[i]["HostStarAgeGyr"]:
            count += 1
    return count

''' 
Iterates through the list of exoplanets and finds the planet 
which has a star and is the hottest star among all of the
exoplanets. Returns the Planet Identifier
'''
def planet_with_hottest_star(data):
    hottestStarTemp = 0
    hottestPlanetID = ""
    
    for i in range(0, len(data)):
        if(data[i]["HostStarTempK"] and data[i]["HostStarTempK"] > hottestStarTemp):
            hottestStarTemp = data[i]["HostStarTempK"]
            hottestPlanetID = data[i]["PlanetIdentifier"]
    
    return hottestPlanetID

'''
Creates a map of Year to planet discovered count grouped by size.
Structure of the map -> {"Year": [Small Count, Medium Count, Large Count]}
Returns the list of all such mappings.
'''
def planet_discovery_by_year_and_size(data):
    discovery_year_to_count = dict()
    for i in range(0, len(data)):
        discoveredYear = data[i]["DiscoveryYear"] if data[i]["DiscoveryYear"] else "Other"
        jupiterRadii = data[i]["RadiusJpt"]
        if discoveredYear in discovery_year_to_count:
            #update the map
            current_array = discovery_year_to_count[discoveredYear]
            discovery_year_to_count[discoveredYear] = get_radii_class_array(current_array, jupiterRadii)
        else:
            #initialize map
            discovery_year_to_count[discoveredYear] = get_radii_class_array([0, 0, 0], jupiterRadii)
    
    return discovery_year_to_count
      
'''
Updates a static array of size 3 with positions 0->Small, 1->Medium, 2-> Large
based on the jupiterRadii value.
Returns the updated static array.
'''
def get_radii_class_array(current_array, jupiterRadii):
    if(jupiterRadii is ""):
        current_array[2] += 1
    elif(float(jupiterRadii) < 1.0):
        current_array[0] += 1
    elif(float(jupiterRadii) >= 1.0 and float(jupiterRadii) < 2.0): 
        current_array[1] += 1
    else:
        current_array[2] += 1
    
    return current_array

'''
Prints the timeline map consisting of Year to count of planets discovered 
by size. Format of the map:
{"Year": [Small Count, Medium Count, Large Count]}
'''
def print_discovery_timeline(timeline):
    keys = timeline.keys()
    tags = ["Small", "Medium", "Large"]
    for key in keys:
        print("Year:",key)
        countList = timeline[key]
        for i in range(0, 3):
            print("\t"+tags[i]+":"+str(countList[i])) 

'''
Loads exoplanet data from URL and returns it in JSON format.
'''
def load_data():
    url = "https://gist.githubusercontent.com/joelbirchler/66cf8045fcbb6515557347c05d789b4a"\
        "/raw/9a196385b44d4288431eef74896c0512bad3defe/exoplanets"
    #loads json data from url
    response = urlRequest.urlopen(url)
    data = json.loads(response.read().decode())
    return data
        
#Program main controller
def main():
    try:
        print("Loading the info....")
        #loads data from given URL
        data = load_data()

        #Fecthes the number of exoplanets without stars.
        print("Number of planets without Stars:")
        print(number_of_planets_without_stars(data))

        #Fetches the planet identifier orbitting the hottest star
        print("Planet identifier orbitting the hottest star:")
        print(planet_with_hottest_star(data))

        #Fetches planet discovery year grouped by size and creates a map.
        print("Number of small, medium and large planets discovered each year:")
        print_discovery_timeline(planet_discovery_by_year_and_size(data))
    except:
        print("Parse Error:")
        print("Exception occured while fetching data from the URL!")
        traceback.print_exc()
    
if __name__ == "__main__":
    main()