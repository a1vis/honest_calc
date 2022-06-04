def calc(v1, v2, v3):
    if v3 == "+":
        return v1 + v2
    if v3 == "-":
        return v1 - v2
    if v3 == "*":
        return v1 * v2
    if v3 == "/":
        return v1 / v2


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msgs[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msgs[7]
    if (v1 == 0 or v2 == 0) and v3 in "*+-":
        msg += msgs[8]
    if msg != "":
        msg = msgs[9] + msg
    print(msg)


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


memory = float(0)
msgs = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)"
]
while True:
    x, operator, y = input(msgs[0]).split()
    try:
        x = memory if x == "M" else float(x)
        y = memory if y == "M" else float(y)
        result = calc(x, y, operator)
        check(x, y, operator)
        print(result)
        if input(msgs[4]) == "y":
            if is_one_digit(result):
                msg_index = 10
                while True:
                    answer = input(msgs[msg_index])
                    if answer == "y":
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        memory = result
                        break
                    if answer == "n":
                        break
            if not is_one_digit(result):
                memory = result
        if input(msgs[5]) == "n":
            break
    except ValueError:
        print(msgs[1])
    except ZeroDivisionError:
        print(msgs[3])
