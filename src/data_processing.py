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
    df_season = df[df['season'] > 2020]
    df_pos = df_season[df_season['position'] == 'WR']
    df_snaps = df_pos[df_pos['offense_snaps'] > 50]
    df_unique = df_snaps.drop_duplicates()
    
    return df_unique

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
    df = filter_by_position(df, 'RB')

    save_processed_csv(df, processed_csv)
