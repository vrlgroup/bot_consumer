from sheet.read import read_sheet

class GroupIdentifier:
    def __init__(self, id, pattern, min_range, max_range):
        self.id = id
        self.pattern = pattern
        self.min_range = min_range
        self.max_range = max_range


def buildCsvToGroups():
    instances = 1
    rows = read_sheet('001')
    groups = make_groups_from_rows(rows)

    return instances, rows, groups


def make_groups_from_rows(rows) -> list:
    pattern_ids = []
    groups = []

    for k, _ in enumerate(rows):
        if k % 4 == 0:
            pattern_ids.append(k)

    for id in pattern_ids:
        pattern = rows[id]
        min_range = rows[id + 1]
        max_range = rows[id + 2]

        model = GroupIdentifier(id, pattern, min_range, max_range)
        groups.append(model)

    return groups
