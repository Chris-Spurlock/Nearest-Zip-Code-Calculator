from math import radians, cos, sin, asin, sqrt
import pandas as pd

zip_df = pd.read_csv('zip_w_lat-long.csv')

# Todo: try block to ensure zip is valid
def find_zips(zipcode):
    """
    Take a ZIP code as a parameter and find all other ZIP codes within a 200-mile radius.
    """
    target_zip = int(zipcode)
    target_lat = zip_df.loc[zip_df['zip'] == target_zip]['lat']
    target_long = zip_df.loc[zip_df['zip'] == target_zip]['long']

    zip_df['distance'] = haversine_distance(target_lat, target_long, zip_df['lat'], zip_df['long'])
    nearest_zips = zip_df[zip_df['distance'] <= 200]

    return nearest_zips

# Calculate distance between two sets of lat/long coordinates
# Credit: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine_distance(lat1, long1, lat2, long2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])

    # haversine formula 
    dlon = long2 - long1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3959 # Radius of earth in mi
    return c * r

print(find_zips('40205'))