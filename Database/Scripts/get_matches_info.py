import psycopg2
import soccerdata as sd
import pandas as pd
from soccerdata import _common
from database import connect_to_database,database_engine

FILES_PATH = 'C:/Users/isaac/Documents/APuestasJair/Pruebas/'

def get_league_id(league_name):
    conn = connect_to_database()
    if conn is not None:
        cursor = conn.cursor()
        query = "SELECT league_id FROM leagues WHERE league_name = %s"
        cursor.execute(query, (league_name,))
        league_id = cursor.fetchone()[0]
        conn.close()
        return league_id
    else:
        print("Error: Unable to connect to the database.")
        return None

def get_teams_data(league_id):
    conn = database_engine()
    if conn is not None:
        query = "SELECT team_name, team_id FROM teams WHERE league_id = %s" %(league_id)
        df_team_ids = pd.read_sql_query(query, conn)
        conn.dispose()
        return df_team_ids
    else:
        print("Error: Unable to connect to the database.")
        return None


def get_matches_data(league_name, season):
    try:
        fbref_client = sd.FBref(leagues=league_name, seasons=season)
        matches_data = fbref_client.read_schedule()
        matches_data = matches_data.sort_values(by=['date', 'time'])
        matches_data = matches_data.drop(['home_xg','score','away_xg','attendance','venue','referee','match_report','notes'], axis=1)
        matches_data = matches_data.rename(columns={'game_id': 'match_id'})
        return matches_data
    except Exception as e:
        print("Error:", e)
        return None

def clean_matches_data(league_id,matches,teams):
    matches['league_id'] = league_id
    matches = pd.merge(matches, teams, left_on='home_team', right_on='team_name', how='left')
    matches = pd.merge(matches, teams, left_on='away_team', right_on='team_name', how='left',suffixes=('', '_away'))
    matches['game_id_feik'] = matches.apply(_common.make_game_id, axis=1)

    matches = matches.rename(columns={
        'date': 'match_date',
        'time': 'match_time',
        'team_id': 'home_team_id',
        'team_id_away': 'away_team_id'
    })

    return matches

def save_matches_db(matches):
    conn = database_engine()
    if conn is not None:
        columns_to_insert = ['match_id', 'league_id', 'home_team_id', 'away_team_id', 'round', 'week', 'day', 'match_date', 'match_time']  
        matches[columns_to_insert].to_sql('matches', con=conn, if_exists='append', index=False)
        conn.dispose()
    else:
        print("Error: Unable to connect to the database.")


def main():
    league_name = "Liga MX"
    league_id = get_league_id(league_name)
    teams = get_teams_data(league_id)
    
    league_name_fbref="Liga-mx"
    season=2324
    matches = get_matches_data(league_name_fbref,season)
    
    matches = clean_matches_data(league_id,matches,teams)
    matches.to_csv(FILES_PATH + 'matchesFilter.csv', index=False)    

    #save_matches_db(matches)
        
if __name__ == "__main__":
    main()