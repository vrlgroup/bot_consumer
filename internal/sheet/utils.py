
def remove_row_useless_chars(row) -> str:
    rowAsString = str(row)
    rowAsString = rowAsString.replace("'", '')
    rowAsString = rowAsString.replace('[', '')
    rowAsString = rowAsString.replace(']', '')
    return rowAsString