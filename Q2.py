# 讀取輸入中的隊伍數量
number = int(input(""))
# 初始化合法隊伍總數為 0
res = 0

# 使用迴圈處理每個隊伍的人數
for i in range(number):
    # 讀取每個隊伍的人數
    member = int(input(""))
    # 檢查人數是否為 3 的倍數且大於 0
    if member % 3 == 0 and member > 0:
        # 如果符合條件，將合法隊伍總數加一
        res = res + 1

# 輸出合法隊伍總數
print(res)