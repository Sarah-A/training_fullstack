
DROP VIEW IF EXISTS players_standings, players_wins,players_matches;

select * 
from players left join matches
on players.id = matches.winner or players.id = matches.loser;


--select players.id , count(matches.winner) as wins
--from players left join matches
--	 on players.id = matches.winner
--group by players.id
--order by wins desc;


insert into players (name) values ('player 1');
insert into players (name) values ('player 2');
insert into players (name) values ('player 3');
insert into players (name) values ('player 4');
insert into players (name) values ('player 5');
insert into players (name) values ('player 6');


insert into matches values('1','2');
insert into matches values('3','1');

-- View: players_wins
--		 all the players with the number of wins
create view players_wins as
select players.id , count(matches) as wins
from players left join matches
	 on players.id = matches.winner
group by players.id;


-- View: players_matches
-- 		 all the players, with the number of matches they played
create view players_matches as
select players.id , count(matches) as matches
from players left join matches
	 on players.id = matches.winner or players.id = matches.loser
group by players.id;

select * from players_wins;
select * from players_matches;

create view players_standings as
select players.id as id , players.name as name, players_wins.wins as wins , players_matches.matches as matches
from players , players_wins, players_matches
where players.id = players_wins.id and players.id = players_matches.id;


select * from players_standings;

select * from players_standings
order by wins desc;

--create view all_pairing as
--select player1.id as player1_id, player2.id as player2_id, sum(player1.wins + player2.wins) as combined_wins
--from players_wins as player1 , players_wins as player2
--where player1.id != player2.id
--group by player1_id , player2_id
--order by (combined_wins) desc;

--select distinct on (player1_id) * from all_pairing;








