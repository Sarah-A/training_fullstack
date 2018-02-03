--------------------------------------------------------------------------------------------------
--		clean up previous runs:					  
--------------------------------------------------------------------------------------------------

-- remove previous definitions:
DROP VIEW IF EXISTS  players_standings_order_on_wins_desc, players_standings, players_wins, players_matches;
DROP TABLE IF EXISTS  players, matches;

-- remove the database if exist:
-- 1. close all connections to the database (except this one):
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'tournament'
  AND pid <> pg_backend_pid();
-- 2. disconnect from the database (by connecting to the default PostgreSQL database):
\c postgres
-- 3. drop the database:
DROP DATABASE IF EXISTS tournament;
