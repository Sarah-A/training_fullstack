#!/usr/bin/env python
# -*- coding: cp1252 -*-
# 
# tournament.py -- implementation of a Swiss-system tournament
#
""" A library to manage tournament pairing and results

    Author: Sarah Ashri                 Date: 12.2015
    This module is part of the data-base project in the FullStack NanoDegree in Udacity.

    Public functions:
    deleteMatches:  delete all the matches from the database. Return: None
    deletePlayers:  delete all the players from the database. Return: None
    countPlayers:   return the number of players currently registered
    registerPlayer: add a player to the tournament database
    playerStanding: Returns a list of the players and their win records, sorted by wins
    reportMatch:    add the results of a single match to the database. Return: None
    swissPairing:   Returns a list of pairs of players for the next round of a match

    Notes:
    *   The module currently supports only one tournament at a time. and needs to be cleared before stating
        the next tournament.
    *   The module doesn't handle odd number of players. If there is an odd number of players,
        the player with the lowest number of wins will not participate in the next match.
    *   Doesn't support 'draw' result in a match.
        
"""

import psycopg2


def _query_database(query, is_read ,*argv):
    """ Send a query to the database. 
    
    Includes all the required commands to connect, update and close the DB.
    
    Args:
      query: the query to send to the database.
      is_read: is the query a read query (if False - this is a write query that changes the DB data)
      *argv: additional paraments to pass to the execute command.
    """
    results = [[0]]
    try:
        conn = psycopg2.connect("dbname=tournament")
        cursor = conn.cursor()
        cursor.execute(query, argv[0])
        if is_read:
            results = cursor.fetchall()
        else:
            # write command:
            conn.commit()            
        conn.close()
    except Exception as e:
        print("Query Failed: {0}".format(e))
    return results

def _read_database( query, *argv):
    """ send a query to the database in order to read back data from it """
    return _query_database(query, True, argv)

def _write_database(query, *argv):
    """ send a query to the database that changes the data base (e.g. add/remove data) """
    #print("argv = {0}".format(argv))
    _query_database(query, False, argv)

def deleteMatches():
    """Remove all the match records from the database."""
    _write_database("DELETE FROM matches;")
   

def deletePlayers():
    """Remove all the player records from the database."""
    _write_database("DELETE FROM players;")
    

def countPlayers():
    """Returns the number of players currently registered."""
    count = _read_database("SELECT COUNT(*) FROM players;")
    return count[0][0]    

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    _write_database("INSERT INTO players (name) VALUES (%s)", name)
    


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    return _read_database("SELECT * FROM players_standings_order_on_wins_desc")
                            

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    _write_database("INSERT INTO matches VALUES(%s,%s)",winner,loser)
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    pairing = [(standings[i][0],standings[i][1],standings[i+1][0],standings[i+1][1]) 
               for i in range(0,len(standings)-1,2)]
    return pairing
    
    
        
    


