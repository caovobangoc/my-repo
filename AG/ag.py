import os
import sys
import re

# code
option = ["--case-sensitive"]

# get option, pattern and path:
if sys.argv[1] in option:
    option_input = sys.argv[1]
    pattern = sys.argv[2]
    file = sys.argv[3]
else:
    option_input = []
    pattern = sys.argv[1]
    file = sys.argv[2]


result = {}
colored_pattern = '\033[30;43m' + pattern + '\033[0m'
file_cont = {}
count_line = 0
with open(file, "r") as f:
    for line in f.readlines():
        count_line += 1
        file_cont[count_line] = line

for line in file_cont:  # line in [1, 2, ...]
    if pattern in file_cont[line]:
        result[line] = []

for line in file_cont:  # line in [1, 2, ...]
    if "--case-sensitive" in option_input:
        if pattern in file_cont[line]:
            file_cont[line] =\
             file_cont[line].replace(pattern, colored_pattern)
            a = ('\033[1;33m'+str(line)+'\033[0m')+":"+file_cont[line]
            result[line] = a
    else:
        if pattern.lower() in file_cont[line].lower():
            list_patterns = set(re.findall("(?i)"+pattern, file_cont[line]))
            for patt in list_patterns:
                col_patt = '\033[30;43m'+patt+'\033[0m'
                file_cont[line] = file_cont[line].replace(patt, col_patt)
            a = ('\033[1;33m'+str(line)+'\033[0m')+":"+file_cont[line]
            result[line] = a

sort_line = sorted(list(result.keys()))
for line in sort_line:
    print(result[line][:-1])
