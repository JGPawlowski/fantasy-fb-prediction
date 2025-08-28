import pandas as pd
import os

def load_raw_csv(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File Not Found {file_path}")
    
    df = pd.read_csv(file_path)
    return df



def filter_by_position(df: pd.DataFrame, position: str) -> pd.DataFrame:
    if 'position' not in df.columns:
        raise KeyError('CSV must contain the position column')
    
    # only grab these columns
    df_filtered = df[[
        'player_name_y', 'season', 'week', 'offense_snaps', 'offense_pct', 'team_offense_snaps', 'height', 'weight', 'position', 'receiving_yards', 'yards_after_catch', 'fumble', 'receptions', 'targets', 'receiving_touchdown', 'fantasy_points_ppr', 'fantasy_points_standard', 'adot', 'rec_td_pct',         'yptarget', 'ayptarget', 'total_yards', 'yptouch', 'delta_offense_snaps', 'delta_offense_pct','delta_receiving_yards', 'delta_fantasy_points_ppr', 'delta_fantasy_points_standard','delta_touches', 'delta_total_tds', 'delta_total_yards'
        ]]
    

    # filter by seasons since 2018 and position
    df_filtered = df_filtered.loc[
        (df_filtered['season'] > 2018) &
        (df_filtered['position'] == position)
    ]
    return df_filtered.drop_duplicates()



def save_processed_csv(df: pd.DataFrame, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print('New Processed CSV File Created.')




if __name__ == '__main__':
    raw_csv = '../data/player_stats_offense.csv'
    processed_csv = '../data/processed/processed_weekly_stats_offense.csv'

    # load the raw file
    df = load_raw_csv(raw_csv)

    # filter by the passed in position
    df = filter_by_position(df, 'WR')

    save_processed_csv(df, processed_csv)
