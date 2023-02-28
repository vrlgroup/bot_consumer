from common.groups import GROUPS_PRESETS


def getGroupsSlices(presetID: int) -> list[list[str]]:
    i = 0
    res = []

    keepGoing = True
    while keepGoing:
        gps = getGroupsToForwardByRound(presetID, i)

        if len(gps) == 0:
            keepGoing = False
        else:
            res.append(gps)

        i += 1

    return res


def getGroupsToForwardByRound(presetID: int, currentRound: int):
    groups = GROUPS_PRESETS[presetID]

    startAtIndex = (currentRound * 5)
    endAtIndex = (currentRound * 5) + 5

    if (currentRound == 0):
        startAtIndex = 0
        endAtIndex = 5

    return groups[startAtIndex:endAtIndex]
