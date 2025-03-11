-- Créer une base de données (si ce n'est pas déjà fait)
CREATE DATABASE cycling_data;

-- Se connecter à la base de données
\c cycling_data;

-- Table pour les résultats des courses (Top 10)


-- Table pour les informations des courses
CREATE TABLE races (
    id SERIAL PRIMARY KEY,
    race_name VARCHAR(255),
    date DATE,
    start_time TIME,
    avg_speed_winner FLOAT,
    classification VARCHAR(255),
    race_category VARCHAR(255),
    distance_km FLOAT,
    points_scale INT,
    uci_scale INT,
    profile_score INT,
    vertical_meters INT,
    departure VARCHAR(255),
    arrival VARCHAR(255),
    race_ranking INT,
    startlist_quality_score INT,
    won_how VARCHAR(255)
);

-- Table pour les informations des coureurs
CREATE TABLE riders (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    nationality VARCHAR(255),
    birth_date DATE,
    weight_kg INT,
    height_m INT,
    place_of_birth VARCHAR(255),
    uci_world_rank INT,
    pcs_ranking INT
);
