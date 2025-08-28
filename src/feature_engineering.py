import pandas as pd
import os

def load_processed_csv(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File Not Found {file_path}")
    
    df = pd.read_csv(file_path)
    return df


def rolling_avg(df: pd.DataFrame, window, int = 3) -> pd.DataFrame:
    df = df.sort_values(['player_name_y', 'season', 'week'])
    rolling_cols = [
        'offense_snaps', 'offense_pct', 'team_offense_snaps',
        'receiving_yards', 'yards_after_catch', 'fumble',
        'receptions', 'targets', 'receiving_touchdown',
        'fantasy_points_ppr', 'fantasy_points_standard',
        'adot', 'rec_td_pct', 'yptarget', 'ayptarget',
        'total_yards', 'yptouch',
        'delta_offense_snaps', 'delta_offense_pct',
        'delta_receiving_yards', 'delta_fantasy_points_ppr',
        'delta_fantasy_points_standard', 'delta_touches',
        'delta_total_tds', 'delta_total_yards'
    ]

    for col in rolling_cols:
        df[f'{col}_rolling{window}'] = (
            df.groupby('player_name_y')[col]
              .rolling(window=window, min_periods=1)
              .mean()
              .reset_index(0, drop=True)
        )

    return df

if __name__ == '__main__':
    path = '../data/processed/processed_weekly_stats_offense.csv'
    df = load_processed_csv(path)
    df = rolling_avg(df, 3)
    print(df.head(20))
