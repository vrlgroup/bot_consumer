import csv
from utils.convert import *

def read_sheet(sheet_id='0') -> list:
    rows = []
    with open(f'./docs/group_{sheet_id}.csv', 'r') as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            rowAsString = remove_row_useless_chars(row)
            rows.append(rowAsString)

    return rows


def remove_row_useless_chars(row) -> str:
    rowAsString = str(row)
    rowAsString = rowAsString.replace("'", '')
    rowAsString = rowAsString.replace('[', '')
    rowAsString = rowAsString.replace(']', '')
    return rowAsString

def getCsvGroups():
    instances = 1
    rows = read_sheet('001')
    groups = make_groups_from_rows(rows)

    return instances, rows, groups