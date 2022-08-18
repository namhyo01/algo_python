class User:
    def __init__(self, userNum, balance):
        self.userNum = userNum
        self.money = balance
        self.balance = [[userNum,balance]]
    def inputMoney(self, money):
        users = []
        self.money -= money
        while True:
            hasMoney = self.balance[-1][1]
            if hasMoney >= money:
                users.append([self.balance[-1][0],money])
                self.balance[-1][1] -= money
                break
            else:
                money -= hasMoney
                users.append([self.balance[-1][0],hasMoney])
                self.balance.pop()
               
        return users
        
    def deposit(self, money,totMoney):
        self.money += totMoney
        for i in money:
            self.balance.append(i)

    def revoke(self, userNum):
        for i in range(len(self.balance)):
            if self.balance[i][0] == userNum:
                self.money -= self.balance[i][1]
                

balance = [30, 30, 30, 30]
users = []
for i in range(len(balance)):
    users.append(User(i+1,balance[i]))
transaction = [[1, 2, 10], [2, 3, 20], [3, 4, 5], [3, 4, 30]]

for i in transaction:
    moneys = users[i[0]-1].inputMoney(i[2])
    users[i[1]-1].deposit(moneys,i[2])

abnormal = [1]
for user in abnormal:
    for i in users:
        i.revoke(user)

for user in users:
    print(user.money)