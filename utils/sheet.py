import csv


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
