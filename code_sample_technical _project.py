"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
	# Replace the line below with your code
	'''
	Purpose: Filter through a list dictionaries representing player stats and return qualified games where
				certain criteria are met
	Paramters: 
		game_data (list) - A list of dictionaries representing a certain players shooting stats in a certain game
		true_shooting_cutoff (int) - An int representing the cutoff number which players must meet to qualify a gameID
		player_count (int) - An int representing the cutoff number of players who must meet the true_shooting_cutoff within one game to make that gameID valid
	Return:
		qualified_game_list (list) - A list of gameID's where enough or more than enough players met the true_shooting_cutoff
	'''
	
	
	game_list = []
	qualified_game_list = []
	for dict in game_data:
		
		# Assign stats to that of each player in dictionary
		freeThrowAttempted = dict["freeThrowAttempted"]
		freeThrowMade = dict["freeThrowMade"]
		fieldGoal2Attempted = dict["fieldGoal2Attempted"]
		fieldGoal2Made = dict["fieldGoal2Made"]
		fieldGoal3Attempted = dict["fieldGoal3Attempted"]
		fieldGoal3Made = dict["fieldGoal3Made"]
		
		#calculate true shooting percentage
		total_points = freeThrowMade + (2 * fieldGoal2Made) + (3 * fieldGoal3Made)
		total_field_goal_attmpt = fieldGoal2Attempted + fieldGoal3Attempted
		true_shooting_pct = total_points / (2 * (total_field_goal_attmpt + (.44 * freeThrowAttempted)))
		
		#convert true shooting percentage to an int, as true_shooting_cutoff is an int
		true_shooting_int = true_shooting_pct * 100

		if true_shooting_int >= true_shooting_cutoff:
			game_list.append(dict["gameID"])

	# loop through gameID's in gamelist	
	for gameID in game_list:
		# check if gameID is not already in qualified game list
		if gameID not in qualified_game_list:
			# check if gameID shows up player_count or more times, i.e. check if enough   
			# players met the true shooting cutoff
			if game_list.count(gameID) >= player_count :
				qualified_game_list.append(gameID)

	return qualified_game_list


	
