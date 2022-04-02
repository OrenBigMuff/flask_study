import random


def quiz():
    qa = []
    with open("static/quiz.txt", encoding="utf-8") as f:
        for i in f:
            data = i.rstrip().split(",")
            qa.append(data)

    selected_qa = random.sample(qa, 5)

    return selected_qa


if __name__ == "__main__":
    selected_qa = quiz()
    for i in selected_qa:
        print(i[0], i[1])
