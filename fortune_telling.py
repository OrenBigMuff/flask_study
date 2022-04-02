import random


def fortune_telling():
    kikkyo = {1: "大吉", 2: "中吉", 3: "小吉", 4: "吉", 5: "末吉", 6: "凶"}
    num = random.randint(1, 6)
    result = kikkyo[num]

    text = []
    with open("static/messages.txt", encoding="utf-8") as f:
        for i in f:
            txt_data = i.rstrip().split(" ")
            # print(txt_data)
            text.append(txt_data)

    select_msg = random.choice(text)
    msg = select_msg[0]
    who = select_msg[1]

    return result, msg, who


if __name__ == "__main__":
    result, msg, who = fortune_telling()
    print(result, msg, who)
