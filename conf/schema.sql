--CREATE TABLE user
--(
--	username VARCHAR(64) NOT NULL,
--	passwd_hash VARCHAR(64) NOT NULL,
--	first_name VARCHAR(64) DEFAULT NULL,
--	last_name VARCHAR(64) DEFAULT NULL,
--	email VARCHAR(128) DeFAULT NULL
--);

-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-03-21 12:51:20.437

-- tables
-- Table: actor
CREATE TABLE actor (
    id integer NOT NULL CONSTRAINT actor_pk PRIMARY KEY,
    name integer NOT NULL
);

-- Table: director
CREATE TABLE director (
    id integer NOT NULL CONSTRAINT director_pk PRIMARY KEY,
    name varchar(64) NOT NULL
);

-- Table: film
CREATE TABLE film (
    id integer NOT NULL CONSTRAINT film_pk PRIMARY KEY,
    duration integer NOT NULL,
    date integer NOT NULL,
    grade numeric NOT NULL,
    original_title varchar(64) NOT NULL,
    original_language varchar(64) NOT NULL,
    age integer NOT NULL
);

-- Table: film_actor
CREATE TABLE film_actor (
    actor_id integer NOT NULL,
    film_id integer NOT NULL,
    CONSTRAINT film_actor_actor FOREIGN KEY (actor_id)
    REFERENCES actor (id),
    CONSTRAINT film_actor_film FOREIGN KEY (film_id)
    REFERENCES film (id)
);

-- Table: film_director
CREATE TABLE film_director (
    director_id integer NOT NULL,
    film_id integer NOT NULL,
    CONSTRAINT film_director_director FOREIGN KEY (director_id)
    REFERENCES director (id),
    CONSTRAINT film_director_film FOREIGN KEY (film_id)
    REFERENCES film (id)
);

-- Table: film_genre
CREATE TABLE film_genre (
    film_id integer NOT NULL,
    genre_id integer NOT NULL,
    CONSTRAINT film_gender_film FOREIGN KEY (film_id)
    REFERENCES film (id),
    CONSTRAINT film_gender_gender FOREIGN KEY (genre_id)
    REFERENCES genre (id)
);

-- Table: film_nationality
CREATE TABLE film_nationality (
    nationality_id integer NOT NULL,
    film_id integer NOT NULL,
    CONSTRAINT film_nationality_nationality FOREIGN KEY (nationality_id)
    REFERENCES nationality (id),
    CONSTRAINT film_nationality_film FOREIGN KEY (film_id)
    REFERENCES film (id)
);

-- Table: genre
CREATE TABLE genre (
    name varchar(64) NOT NULL,
    id integer NOT NULL CONSTRAINT genre_pk PRIMARY KEY
);

-- Table: nationality
CREATE TABLE nationality (
    nationality varchar(64) NOT NULL,
    id integer NOT NULL CONSTRAINT nationality_pk PRIMARY KEY
);

-- Table: studio
CREATE TABLE studio (
    name varchar(64) NOT NULL,
    id integer NOT NULL CONSTRAINT studio_pk PRIMARY KEY,
    zip_code varchar(64) NOT NULL,
    country varchar(64) NOT NULL,
    website varchar(255) NOT NULL
);

-- Table: film_studio
CREATE TABLE film_studio (
    studio_id integer NOT NULL,
    film_id integer NOT NULL,
    CONSTRAINT studio_id_studio FOREIGN KEY (studio_id)
    REFERENCES studio (id),
    CONSTRAINT studio_id_film FOREIGN KEY (film_id)
    REFERENCES film (id)
);

-- Table: user
CREATE TABLE user (
    id integer NOT NULL CONSTRAINT user_pk PRIMARY KEY,
    username varchar(64) NOT NULL,
    passwd_hash varchar(64) NOT NULL,
    first_name varchar(64) NOT NULL,
    last_name varchar(64) NOT NULL,
    email varchar(128) NOT NULL,
    role_id integer NOT NULL,
    CONSTRAINT role_id_user FOREIGN KEY (role_id)
    REFERENCES role (id)
);

-- Table: role
CREATE TABLE role (
    name varchar(64) NOT NULL,
    id integer NOT NULL CONSTRAINT role_pk PRIMARY KEY
);

-- End of file.

-- Add to roles
INSERT INTO role (id, name) VALUES (1,"admin");
INSERT INTO role (id, name) VALUES (2,"user");

-- Add to users
INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) VALUES ('jojostoche','7110eda4d09e062aa5e4a390b0a572ac0d2c0220','Joachim','Bach','yolo@yolo.yolo','1');
INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) VALUES ('totoche','7110eda4d09e062aa5e4a390b0a572ac0d2c0220','Theo','Mosca','toto@toto.toto','1');

-- Add to genre
INSERT INTO genre (name) VALUES ('horror');
INSERT INTO genre (name) VALUES ('comedy');
INSERT INTO genre (name) VALUES ('action');
INSERT INTO genre (name) VALUES ('thriller');
INSERT INTO genre (name) VALUES ('animation');
INSERT INTO genre (name) VALUES ('love story');
INSERT INTO genre (name) VALUES ('science fiction');

-- Add Studio

INSERT INTO studio (name, zip_code, country, website) VALUES ('Paramount Pictures France','20-24, rue Jacques Ibert
92300 Levallois-Perret','France','http://www.paramountpictures.fr/');

-- Add Actor

INSERT INTO actor (name) VALUES ('Jovan Adepo');


