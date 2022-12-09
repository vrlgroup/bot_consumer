from models.model import GroupIdentifier

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
