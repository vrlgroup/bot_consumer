from time import sleep


def wait(sec: int, reason: str = ""):
    k = 0
    print(" ")
    while k <= sec:
        print(f"[{k}/{sec}] - {reason}")
        sleep(1)

        k += 1
