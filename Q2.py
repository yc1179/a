
number = int(input("")) # 讀取輸入中的隊伍數量

res = 0 # 初始化合法隊伍總數為 0

for i in range(number): # 使用迴圈處理每個隊伍的人數
        member = int(input("")) # 讀取每個隊伍的人數
        if member % 3 == 0 and member > 0: # 檢查人數是否為 3 的倍數且大於 0
                res = res + 1# 如果符合條件，將合法隊伍總數加一
print(res) # 輸出合法隊伍總數