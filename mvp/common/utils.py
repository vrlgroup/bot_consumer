import math

def getNumberOfForwardPerMessage(groups: list[str], maxPerRound : int = 5) -> int:
    return math.ceil(len(groups) / maxPerRound)
