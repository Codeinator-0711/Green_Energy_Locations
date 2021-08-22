import pandas as pd

def addinfo(weather_df, station_df, add):
    '''
    returns updated weather dataframe with added info about the station
    :param weather_df: dataframe with weather data, must include station id
    :param station_df: dataframe with station info, must include station id
    :param add: list of info to add to the weather_df
    '''
    cols = add
    if not station_df.index.name == 'id':
        if not 'id' in cols:
            cols.append('id')
    to_join = station_df[cols].copy()
    if 'id' in to_join.columns:
        to_join.set_index('id',inplace = True, drop = True)
    if 'location' in cols:
        to_join.loc[:,'latitude'] = [eval(x)[0] for x in to_join.location]
        to_join.loc[:,'longitude'] = [eval(x)[1] for x in to_join.location]
    added_df = pd.merge(weather_df,to_join,left_on='id',right_on='id')
    return added_df