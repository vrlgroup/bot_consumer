from internal.models.group import *
import csv


def makeGroupNamesFromCSVRow(row) -> list[str]:
    groupPatternPrefix = row[0]
    groupMinID = int(row[1])
    groupMaxID = int(row[2])

    res: list[str] = []
    for k in range(groupMinID, groupMaxID + 1):
        res.append(f"{groupPatternPrefix}{k:02}")

    return res


def readCSVWithSuffix(csvID: str) -> list[str]:
    groups: list[str] = []

    with open(f'./internal/sheet/csv/group_{csvID}.csv', 'r') as file:
        csvreader = csv.reader(file)

        for i, row in enumerate(csvreader):
            if i > 0:
                for groupSuffix in makeGroupNamesFromCSVRow(row):
                    groups.append(groupSuffix)

    return groups
