# Supplement functions Initialization

def parser(a_file):
    with open(a_file) as f:
        lines = f.readlines()
        lines = [line.strip('\n').split() for line in lines]

        return lines
