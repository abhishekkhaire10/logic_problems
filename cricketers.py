class Player():
    def __init__(self, playerName, playerCountry, playerAge,
    noOfMatches, noOfRuns, noOfWickets):


        self.playerName = playerName
        self.playerCountry = playerCountry
        self.playerAge = playerAge
        self.noOfMatches = noOfMatches 
        self.noOfRuns = noOfRuns 
        self.noOfWickets = noOfWickets


class Team():
    def getMinRuns(self, playerObj):
        runs = []
        for player in playerObj:
            runs.append(player.noOfRuns)
        return min(runs)

    def getMaxWickets(self, playerObj):
        wickets = []
        for player in playerObj:
            wickets.append(player.noOfWickets)
        return max(wickets)


if __name__ == '__main__':
    no_players = int(input())
    player_objs = []
    for i in range(0, no_players):
        playerName = input()
        playerCountry = input()
        playerAge = input()
        noOfMatches = int(input())
        noOfRuns = int(input())
        noOfWickets = int(input())
        player_objs.append(Player(playerName, playerCountry, playerAge,
    noOfMatches, noOfRuns, noOfWickets))

    team = Team()
    minimum_runs = team.getMinRuns(player_objs)
    maximum_wickets = team.getMaxWickets(player_objs)

    print('''Minimum Runs: {}
              Maximum Wickets: {}'''.format(minimum_runs, maximum_wickets))