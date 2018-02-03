-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--------------------------------------------------------------------------------------------------
--		clean up previous runs:					  
--------------------------------------------------------------------------------------------------

\i delete_tournament.sql

--------------------------------------------------------------------------------------------------
--		Create Database:					  
--------------------------------------------------------------------------------------------------

-- create the tournament data base:
CREATE DATABASE tournament;

-- connect to the database:
\c tournament;

--------------------------------------------------------------------------------------------------
--		Create Tables:					  
--------------------------------------------------------------------------------------------------

-- create players table with is as an automatically generated primary key:
CREATE TABLE players(
					 id SERIAL PRIMARY KEY,
					 name TEXT NOT NULL);
					 
-- create matches table.
CREATE TABLE matches(
					  winner INTEGER REFERENCES players(id) ON DELETE CASCADE,
					  loser INTEGER REFERENCES players(id) ON DELETE CASCADE,
					  CONSTRAINT check_keys PRIMARY KEY(winner,loser),
					  CONSTRAINT check_players CHECK(winner <> loser));

--------------------------------------------------------------------------------------------------
--		Create Views:					  
--------------------------------------------------------------------------------------------------

-- View: players_wins
--		 total wins for every player
CREATE VIEW players_wins AS
SELECT players.id , COUNT(matches) AS wins
FROM players LEFT JOIN matches
	 ON players.id = matches.winner
GROUP BY players.id;


-- View: players_matches
-- 		 total matches for every player
CREATE VIEW players_matches AS
SELECT players.id , COUNT(matches) AS matches
FROM players LEFT JOIN matches
	 ON players.id = matches.winner OR players.id = matches.loser
GROUP BY players.id;


-- View: players_standings
--		 total wins and matches for every player
CREATE VIEW players_standings AS
SELECT players.id , players.name , players_wins.wins , players_matches.matches 
FROM players , players_wins, players_matches
WHERE players.id = players_wins.id AND players.id = players_matches.id;

-- View: players_standings_order_on_wins_desc
CREATE VIEW players_standings_order_on_wins_desc AS
SELECT * FROM players_standings
ORDER BY wins DESC;



