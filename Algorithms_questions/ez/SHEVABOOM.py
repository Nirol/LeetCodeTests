
def is_boom(number):
    if number % 7 == 0:
        return True
    num_string = str(number)
    if "7" in num_string:
        return True
    return False


def shevaBoom(target):
    for i in range(1, target+1):
        if is_boom(i):
            print ("boom")
        else:
            print(i)


if (__name__ == "__main__"):
    shevaBoom(83)