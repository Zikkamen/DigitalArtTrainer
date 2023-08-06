CREATE TABLE IF NOT EXISTS exercises_overview
(
    id serial PRIMARY KEY,
    exercise_name VARCHAR(128) NOT NULL,
    exercise_url VARCHAR(128) NOT NULL,
    image_url VARCHAR(128) NOT NULL,
    exercise_description VARCHAR(256)
);
CREATE TABLE IF NOT EXISTS sub_exercises
(
    id serial PRIMARY KEY,
    exercise_name VARCHAR(128) NOT NULL,
    exercise_url VARCHAR(128) NOT NULL,
    image_url VARCHAR(128) NOT NULL,
    exercise_description VARCHAR(256),
    exercise_type VARCHAR(128)
);
CREATE TABLE IF NOT EXISTS exercise_repository
(
    id BIGINT PRIMARY KEY,
    owner_id VARCHAR(256) NOT NULL,
    exercise_type VARCHAR(128) NOT NULL,
    sub_exercise_type VARCHAR(128) NOT NULL,
    score VARCHAR(128),
    creation_epoch BIGINT
);
CREATE TABLE IF NOT EXISTS exercise_information
(
    id serial PRIMARY KEY,
    exercise_type VARCHAR(128) NOT NULL,
    sub_exercise_type VARCHAR(128) NOT NULL,
    exercise_tasks VARCHAR(512),
    exercise_name VARCHAR(128),
    exercise_misc_files VARCHAR(512),
    exercise_description VARCHAR(512)
);