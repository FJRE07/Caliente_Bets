CREATE TABLE leagues (
    league_id SERIAL PRIMARY KEY,
    league_name VARCHAR(255) NOT NULL,
    country VARCHAR(255),
    description TEXT,
    logo_url VARCHAR(255)
);

CREATE TABLE teams (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(255) NOT NULL,
    league_id INT REFERENCES leagues(league_id),
    logo_url VARCHAR(255)
);

CREATE TABLE matches (
    match_id SERIAL PRIMARY KEY,
    league_id INT REFERENCES leagues(league_id),
    home_team_id INT REFERENCES teams(team_id),
    away_team_id INT REFERENCES teams(team_id),
    match_date DATE,
    match_time TIME,
    location VARCHAR(255),
    result VARCHAR(50),
    home_team_goals INT,
    away_team_goals INT,
    match_status VARCHAR(50)
);

CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    team_id INT REFERENCES teams(team_id),
    player_name VARCHAR(255) NOT NULL,
    number INT,
    country VARCHAR(255),
    position VARCHAR(50),
    age INT,
    date_updated DATE
);

CREATE TABLE players_stats (
    player_stats_id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(player_id),
    date_updated DATE,
    matches_played INT,
    starting_matches INT,
    minutes_played INT,
    minutes_played_90 DECIMAL(10, 2),
    goals_scored INT,
    assists INT,
    goals_plus_assists INT,
    goals_excluding_penalties INT,
    penalty_kicks_taken INT,
    penalty_kicks_attempted INT,
    yellow_cards INT,
    red_cards INT,
    expected_goals DECIMAL(10, 2),
    non_penalty_expected_goals DECIMAL(10, 2),
    expected_assisted_goals DECIMAL(10, 2),
    non_penalty_expected_goals_plus_expected_assisted_goals DECIMAL(10, 2),
    progressive_carries INT,
    progressive_passes INT,
    progressive_passes_received INT,
    goals_per_90 DECIMAL(10, 2),
    assists_per_90 DECIMAL(10, 2),
    goals_plus_assists_per_90 DECIMAL(10, 2),
    goals_excluding_penalties_per_90 DECIMAL(10, 2),
    goals_excluding_penalties_plus_assists_per_90 DECIMAL(10, 2),
    expected_goals_per_90 DECIMAL(10, 2),
    expected_goals_excluding_penalties_per_90 DECIMAL(10, 2),
    expected_goals_plus_assists_per_90 DECIMAL(10, 2),
    expected_goals_non_penalty_per_90 DECIMAL(10, 2),
    expected_goals_non_penalty_plus_expected_assisted_goals_per_90 DECIMAL(10, 2)
);

CREATE TABLE players_matches_stats (
    player_match_stats_id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(player_id),
    match_id INT REFERENCES matches(match_id),
    minutes_played INT,
    goals INT,
    assists INT,
    penalty_taken INT,
    penalty_tries INT,
    total_shots INT,
    shots_on_target INT,
    yellow_card INT,
    red_card INT,
    touches INT,
    tackles INT,
    interceptions INT,
    locks INT,
    completed_passes INT,
    tried_passes INT,
    prog_passes INT,
    feet_control INT,
    carries INT,
    dribble_attempts INT,
    successful_dribbles INT,
    pass_distance_covered INT,
    pass_distance_towards_goal INT,
    short_passes_completed INT,
    short_passes_attempted INT,
    medium_passes_completed INT,
    medium_passes_attempted INT,
    large_passes_completed INT,
    large_passes_attempted INT,
    passes_to_assisted_shots INT,
    completed_passes_final_third INT,
    completed_passes_18_yard_box INT,
    crosses_completed_18_yard_box INT,
    completed_crosses_18_yard_box INT,
    completed_passes_towards_goal INT,
    live_ball_passes INT,
    live_ball_set_pieces INT,
    free_kick_attempted_passes INT,
    pass_sent_between_defenders INT,
    long_passes_covering_40_yards INT,
    offensive_crossed_passes INT,
    corner_kicks INT,
    ball_regained_tackles INT,
    tackles_defensive_third INT,
    tackles_middle_third INT,
    tackles_attacking_third INT,
    dribblers_tackled INT,
    failed_challenges_plus_dribblers_tackled INT,
    dribblers_tackled_divided_by_attempts DECIMAL(10, 2),
    unsuccessful_dribble_challenges INT,
    shots_blocked INT,
    passes_blocked INT,
    players_tackled_plus_interceptions INT,
    clearances INT,
    errors_lead_to_opponent_shots INT,
    touches_defensive_penalty_area INT,
    touches_attacking_penalty_area INT,
    live_ball_touches INT,
    distance_covered_feet_control INT,
    distance_covered_feet_control_towards_goal INT,
    times_failed_gain_control INT,
    times_lost_control_after_tackle INT,
    times_successful_pass_received INT,
    fouls_committed INT,
    fouls_received INT,
    offsides INT,
    crossed_passes INT,
    goals_against INT,
    loose_balls_recovered INT,
    aerials_won INT,
    aerials_lost INT
);

CREATE TABLE match_odds (
    match_odds_id SERIAL PRIMARY KEY,
    match_id INT REFERENCES matches(match_id),
    home_team_win_odds DECIMAL(10, 2),
    draw_odds DECIMAL(10, 2),
    away_team_win_odds DECIMAL(10, 2)
);

CREATE TABLE match_stats (
    match_stats_id SERIAL PRIMARY KEY,
    match_id INT REFERENCES matches(match_id),
    goals_scored INT,
    total_shots INT,
    shots_on_target INT,
    shots_off_target INT,
    shooting_percentage DECIMAL(10, 2),
    goals_per_shot DECIMAL(10, 2),
    goals_per_shots_on_target DECIMAL(10, 2),
    average_shot_distance DECIMAL(10, 2),
    free_kick_attempts INT,
    penalty_attempts INT,
    penalty_goals INT,
    expected_goals DECIMAL(10, 2),
    expected_goals_without_penalties DECIMAL(10, 2),
    expected_goals_per_penalty_attempt DECIMAL(10, 2),
    goals_minus_expected_goals DECIMAL(10, 2),
    goals_without_penalties_minus_expected_goals DECIMAL(10, 2)
);

CREATE TABLE picks (
    pick_id SERIAL PRIMARY KEY,
    match_id INT REFERENCES matches(match_id),
    percentage_home DECIMAL(10, 2),
    percentage_draw DECIMAL(10, 2),
    percentage_away DECIMAL(10, 2),
    home DECIMAL(10, 2),
    draw DECIMAL(10, 2),
    away DECIMAL(10, 2),
    min DECIMAL(10, 2),
    max DECIMAL(10, 2),
    sd DECIMAL(10, 2),
    average DECIMAL(10, 2),
    max_min DECIMAL(10, 2)
);