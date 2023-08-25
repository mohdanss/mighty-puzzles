'''
    There's an algorithms tournament taking place in which teams of programmers
    compete against each other to solve algorithmic problems as fast as possible.
    Teams compete in a round robin, where each team faces off against all other
    teams. Only two teams compete against each other at a time, and for each
    competition, one team is designated the home team, while the other team is the
    away team. In each competition there's always one winner and one loser; there
    are no ties. A team receives 3 points if it wins and 0 points if it loses. The
    winner of the tournament is the team that receives the most amount of points.


    Given 
    -> An array of pairs representing the teams that have competed against each other.
    -> An array containing the results of each competition
    
    Write a function that returns the winner of the tournament. The input arrays are named
    competitions and results, respectively. The competitions array has elements in the form 
    of [homeTeam, awayTeam], where each team is a string of at most 30 characters representing 
    the name of the team. The results array contains information about the winner of each 
    corresponding competition in the competitions array. Specifically, results[i] denotes the 
    winner of competitions[i], where a 1 in the results array means that the home team in the 
    corresponding competition won and a 0 means that the away team won.

    Sample:
        input: competitions = [
            ['HTML', 'C#'],
            ['C#', 'Python'],
            ['Python', 'Html'],
        ]
        result = [0, 0, 1]
        output: Python

    Note: 

    -> Make sure to make it as optimized as possible, both time and space complexity wise.
    -> Take a deep breath, put aside your 'imposter-self', and give it a go ;)
'''


def tournamentWinner(competitions, result):
    pointsTable = dict()

    idx = 0
    while idx < len(result):
        if result[idx] == 1:  # home team wins
            if competitions[idx][0] in pointsTable:
                pointsTable[competitions[idx][0]] += 3
            else:
                pointsTable[competitions[idx][0]] = 3
        else:
            if competitions[idx][1] in pointsTable:
                pointsTable[competitions[idx][1]] += 3
            else:
                pointsTable[competitions[idx][1]] = 3
        idx += 1

    return max(pointsTable, key=lambda key: pointsTable[key])




print(tournamentWinner([
    ['HTML', 'C#'],
    ['C#', 'Python'],
    ['Python', 'HTML'],
], [0, 0, 1]))

'''
Approach: We need to keep track of maximum value after each competition,
and after iterating all, we can extract the key with maximum value.

n is no. of matches
k is no. of teams.
Time complexity: O(n) + O(k) = O(n)
Space Complexity: O(k)

'''
