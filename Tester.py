import ExoplanetInfoParser as exoplanets
import urllib, json
import urllib.request as urlRequest

def test_planets_without_stars(data):
    print("Function test_planets_without_stars")
    noOfplanets = exoplanets.number_of_planets_without_stars(data)
    if noOfplanets == 30:
        print("Number of planets: 30")
        print("Pass!")
        print("------")
    else:
        print("Fail!"+str(noOfPlanets))
        print("------")

def test_planet_hottest_star(data):
    print("Function test_planet_hottest_star")
    planet_ID = exoplanets.planet_with_hottest_star(data)
    if planet_ID == "V391 Peg b":
        print("Hottest Planet: V391 Peg b")
        print("Pass!")
        print("------")
    else:
        print("Fail!"+planet_ID)
        print("------")

def test_timeline(data):
    print("Function test_timeline")
    timeline_map = exoplanets.planet_discovery_by_year_and_size(data)
    if len(timeline_map) == 28:
        print("Pass!")
        print("------")
    else:
        print("Fail!"+str(len(map)))
        print("------")
    
def main():
    data = exoplanets.load_data()
    test_planets_without_stars(data)
    test_planet_hottest_star(data)
    test_timeline(data)

if __name__ == "__main__":
    main()