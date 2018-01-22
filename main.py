import random

print("狗哥模擬猜拳2018")

class Match:
    def __init__(self):
        self.win_times = 0
        self.lose_times = 0
        self.draw_times = 0

    def matchStart(self, playerChoice):

        print("你的出拳", playerChoice)

        self.playerChoice = int(playerChoice)
        self.com_choice = random.randint(0, 2)
        print("電腦選擇", self.com_choice)

        if playerChoice == (self.com_choice + 1) % 3:
            print("淫了")
            self.win_times = self.win_times + 1
            print(self.win_times)

        elif playerChoice == self.com_choice:
            print("平手")
            self.draw_times = self.draw_times + 1
            print(self.draw_times)

        elif playerChoice == 4:
            menu()

        else:
            print("輸了")
            self.lose_times = self.lose_times + 1
            print(self.lose_times)
        menu()

    def matchLog(self):
        return(self.win_times, self.lose_times, self.draw_times)

def matchmakechoice():
    msg = "\n請出拳 [0]剪刀 [1]石頭 [2]布"
    n = int(input(msg))
    # print(n)
    Match().matchStart(n)
    # return False

def menu():
    while True:
        try:
            menu = int(input("\n[1]開始\n[2]遊玩記錄\n選擇選項："))
            break
        except ValueError:
            print("輸入錯誤，請重新選擇。")
    if menu == 1:
        matchmakechoice()
    else:
        log = Match().matchLog()

        print("勝場：" + str(log[0]) + "平手：" + str(log[2]) + "敗場：" + str(log[1]))

menu()
