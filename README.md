Exoplanet data parser script (Python)

* Downloads Kaggle data set from the given URL --> https://gist.githubusercontent.com/joelbirchler/66cf8045fcbb6515557347c05d789b4a/raw/9a196385b44d4288431eef74896c0512bad3defe/exoplanets
* Parses the received JSON data for:
    1) The number of orphan planets (no star).
    2) The name (planet identifier) of the planet orbiting the hottest star.
    3) A timeline of the number of planets discovered per year grouped by size. Use the following groups: “small” is less than 1 Jupiter radii, “medium” is less than 2 Jupiter radii, and anything bigger is considered “large”. For example, in 2004 we discovered 2 small planets, 5 medium planets, and 0 large planets.
    
    and displays info on the command line.

* Instructions to run:
    1) Clone the repository
    2) Navigate to path of the downloaded folder on the command line
    3) Run "python ExoplanetInfoParser.py"
    4) Run "python Tester.py" for results
    5) Required python 3.