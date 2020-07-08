print("               橙子和梨子             ")
temp = input("猜一下我手里有几颗糖,答对了全都给你！")
guess = int(temp)
if guess == 3:
    print("猜对啦！")
    print("3颗糖送给你！")
else:
    print("猜对啦！先给你3颗糖，我还欠你",guess-3,"颗糖。")


