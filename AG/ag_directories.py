import os
import sys
import re

# code
option = ["--case-sensitive", "--hidden"]
base_cwd = os.getcwd()
# get option, pattern and path:
if sys.argv[1] in option:
    if sys.argv[2] in option:
        option_input = option
        pattern = sys.argv[3]
        if len(sys.argv) < 5:
            cwd = os.getcwd()
        else:
            cwd = os.getcwd() + "/" + sys.argv[4]
    else:
        option_input = sys.argv[1]
        pattern = sys.argv[2]
        if len(sys.argv) < 4:
            cwd = os.getcwd()
        else:
            cwd = os.getcwd() + "/" + sys.argv[3]
else:
    option_input = []
    pattern = sys.argv[1]
    if len(sys.argv) < 3:
        cwd = os.getcwd()
    else:
        cwd = os.getcwd() + "/" + sys.argv[2]

list_files = []
# print(list_files)
# create list of all file
# for i in list(os.walk(cwd)):
#     print(i)
for path, subdirs, files in os.walk(cwd):
    for name in files:
        list_files.append(os.path.join(path, name))
# print(list_files)

# if "--hidden" not in  option_input:
    # list_files = [file for file in list_files if "/." not in file]
# print(list_files)
# cut the path(from current directory go in)
for i in range(len(list_files)):
    list_files[i] = list_files[i][len(base_cwd) + 1:]


dict_file = {}
result = {}
count = 0
colored_pattern = '\033[30;43m' + pattern + '\033[0m'

for file in list_files:
    # create a dict with format {position of line: content of that line}
    count_line = 0
    file_cont = {}
    with open(file, "r", errors="replace") as f:
        for line in f.readlines():
            count_line += 1
            file_cont[count_line] = line  # exp: {1: "Toda, ..."}

    # create a key with empty value(to append line has pattern)
    # if pattern is in file
    for line in file_cont:  # line in [1, 2, ...]
        if "--case-sensitive" in option_input:
            if pattern in file_cont[line]:
                result[file] = []
        else:
            if pattern.lower() in file_cont[line].lower():
                result[file] = []

    for line in file_cont:  # line in [1, 2, ...]
        if "--case-sensitive" in option_input:
            if pattern in file_cont[line]:
                file_cont[line] = file_cont[line].replace(pattern, colored_pattern)
                a = ('\033[1;33m'+str(line)+'\033[0m')+":"+file_cont[line]
                result[file].append(a)
        else:
            if pattern.lower() in file_cont[line].lower():
                list_pattern = set(re.findall("(?i)"+pattern, file_cont[line]))
                for patt in list_pattern:
                    col_patt = '\033[30;43m'+patt+'\033[0m'
                    file_cont[line] = file_cont[line].replace(patt, col_patt)
                a = ('\033[1;33m'+str(line)+'\033[0m')+":"+file_cont[line]
                result[file].append(a)

count_blank_line = 0

sort_file = sorted(list(result.keys()))

for file in sort_file:
    sort_line = sorted(list(result[file]))
    print('\033[1;32m' + file + '\033[0m')
    for j in range(len(result[file])):
        if result[file][j][-1:] == "\n":
            print(result[file][j][:-1])
        else:
            print(result[file][j])
    count_blank_line += 1
    if count_blank_line < len(result.keys()):
        print("")
