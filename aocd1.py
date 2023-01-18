input_file = "input.txt"

def load_data(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    return lines

def sum_elfs(lines):
    elfs = []
    elf = []

    for value in lines:
        if value == '\n':
            elfs += [sum(elf)]
            elf = []
            continue
        elf += [int(value)]
    elfs += [sum(elf)]
    return elfs

lines = load_data(input_file)
elfs = sum_elfs(lines)
elfs = sorted(elfs, reverse=True)
print(elfs[0])