from utils.sheet import *
from utils.convert import *

def main():
    instances = 1

    rows = read_sheet('001')
    groups = make_groups_from_rows(rows)
    


if __name__ == "__main__":
    main()
