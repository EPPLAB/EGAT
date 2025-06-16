
import pandas as pd
import os

def load_and_merge(raw_data_dir):
    files = {
        'elevation': 'elevation_data.csv',
        'gw_depth': 'groundwater_depth.csv',
        'land_use': 'land_use.csv',
        'drainage': 'drainage_density.csv',
        'soil': 'soil_permeability.csv',
    }
    dfs = {name: pd.read_csv(os.path.join(raw_data_dir, fname)) for name, fname in files.items()}
    df = dfs['elevation']
    for key in ['gw_depth', 'land_use', 'drainage', 'soil']:
        df = pd.merge(df, dfs[key], on='StationID', how='left')
    return df
