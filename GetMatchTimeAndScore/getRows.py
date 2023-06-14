# return a list of list
def getRows(teamA, score, teamB):
    rows = []
    for i in range(len(teamA)):
        rows.append([teamA[i][0], teamB[i][0],  score[i][3], f"{score[i][0]} - {score[i][2]}"])
    return rows