class Team :
    w = 0.0
    s = 0.0
    def addW(self, w):
        self.w += w
    def addS(self, s):
        self.s += s
    def getPytha(self):
        return self.w*self.w/(self.w*self.w+self.s*self.s)
# return [team1, team2,...,teamn, int(numOfMatch)]
def getInput():
    line = input().split()
    teams = []
    for i in range(int(line[0])):
        team = Team()
        teams.append(team)
    teams.append(int(line[1]))
    return teams
def recordParse(teams):
    record = input().split()
    a = int(record[0])-1
    b = int(record[1])-1
    w = int(record[2])
    s = int(record[3])
    teams[a].addW(w)
    teams[a].addS(s)
    teams[b].addW(s)
    teams[b].addS(w)
def getMaxPytha(teams):
    maxList=[]
    teams.pop()
    for i in teams :
        maxList.append(i.getPytha())
    maxList.sort()
    print(int(maxList[-1]*1000))
    print(int(maxList[0]*1000))
if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        teams = getInput()
        m = teams[-1]
        for i in range(m):
            recordParse(teams)
        getMaxPytha(teams)

