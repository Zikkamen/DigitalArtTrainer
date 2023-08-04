CREATE TABLE IF NOT EXISTS exercises_overview
(
    id serial PRIMARY KEY,
    exercise_name VARCHAR(50) NOT NULL UNIQUE,
    exercise_url VARCHAR(50) NOT NULL,
    image_url VARCHAR(50) NOT NULL,
    exercise_description VARCHAR(256)
);
CREATE TABLE IF NOT EXISTS sub_exercises
(
    id serial PRIMARY KEY,
    exercise_name VARCHAR(50) NOT NULL UNIQUE,
    exercise_url VARCHAR(50) NOT NULL,
    image_url VARCHAR(50) NOT NULL,
    exercise_description VARCHAR(256),
    exercise_type VARCHAR(50)
);
CREATE TABLE IF NOT EXISTS exercise_repository
(
    id serial PRIMARY KEY,
    exercise_type VARCHAR(50) NOT NULL UNIQUE,
    sub_excercise_type VARCHAR(50) NOT NULL,
    exercise_folder_path VARCHAR(256),
    exercise_url VARCHAR(50)
);
CREATE TABLE IF NOT EXISTS exercise
(
    id BIGINT PRIMARY KEY,
    owner_id VARCHAR(256) NOT NULL,
    exercise_type VARCHAR(50) NOT NULL UNIQUE,
    sub_excercise_type VARCHAR(50) NOT NULL,
    creation_epoch BIGINT
);
CREATE TABLE IF NOT EXISTS exercise_information
(
    id serial PRIMARY KEY,
    exercise_type VARCHAR(50) NOT NULL UNIQUE,
    sub_exercise_type VARCHAR(50) NOT NULL,
    exercise_tasks VARCHAR(512),
    exercise_name VARCHAR(50),
    exercise_misc_files VARCHAR(512),
    exercise_description VARCHAR(512)
);