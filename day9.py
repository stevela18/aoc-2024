# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3.12
#     language: python
#     name: py312
# ---

# %%
example = """2333133121414131402"""

# %%
example_2 = "12345"

# %%
import numpy as np

# %%
with open("day9input.txt", "r") as f:
    input_string = f.read()


# %%
def create_file_system(s):
    file_system = []
    count = 0
    for i, c in enumerate(s):
        if i%2==0:
            file_system.extend([count]*int(c))
            count+=1
        else:
            file_system.extend([-1]*int(c))
    return file_system


# %%
file_system = create_file_system(example_2)

# %%
file_system

# %%
empties = np.where(np.array(file_system)<0)[0]
filled = np.where(np.array(file_system)>=0)[0]

# %%
empties

# %%
filled[0]


# %%
def compress(file_system):
    compressed = file_system.copy()
    empties = np.where(np.array(file_system)<0)[0]
    filled = np.where(np.array(file_system)>=0)[0]
    flag = True
    i = len(filled) - 1
    j = 0
    while flag:
        if i < 0:
            flag = False
        elif filled[i] < empties[j]:
            flag = False
        else:
            compressed[empties[j]] = file_system[filled[i]]
            compressed[filled[i]] = -1
            j += 1
            i += -1
    return compressed


# %%
def check_sum(compressed):
    total = 0
    for i, e in enumerate(compressed):
        total += i*e if e>0 else 0
    return total


# %%
check_sum(compress(create_file_system(input_string)))

# %%
s = "00992111777.44.333....5555.6666.....8888.."
s_list = list(s)
s_list = [-1 if x=="." else int(x) for x in s_list ]

# %%
check_sum(s_list)

# %%
file_system = create_file_system(example)

# %%
print(file_system)


# %%
def file_system_intervals(s):
    filled_intervals = []
    empties_intervals = []
    # file_number = 0
    count = 0
    for i, c in enumerate(s):
        new_count = count + int(c)
        if i%2==0:
            filled_intervals.append((count, new_count))
            # file_number += 1
        elif int(c):
            empties_intervals.append((count, new_count))
        count = new_count
    return filled_intervals, empties_intervals


# %%
file_system = create_file_system(example)
filled_intervals, empties_intervals = file_system_intervals(example)


# %%
def compress2(s):
    compressed = create_file_system(s)
    filled_intervals, empties_intervals = file_system_intervals(s)
    for i in range(len(filled_intervals)-1, -1, -1):
        f = filled_intervals[i]
        len_f = f[1] - f[0]
        flag = True
        j = 0
        while (j<len(empties_intervals))&(flag):
            e = empties_intervals[j]
            len_e = e[1] - e[0]
            if len_e >= len_f:
                compressed[e[0]:(e[0]+len_f)] = [i]*len_f
                if len_e == len_f:
                    empties_intervals.remove(e)
                else:
                    empties_intervals[j] = (e[0]+len_f, e[1])
                compressed[f[0]:f[1]] = [-1]*len_f
                while compressed[-1] < 0:
                    compressed = compressed[:-1]
                flag = False
            j+=1
    return compressed


# %%
compressed = compress2(example)

# %%
print(compressed)

# %%
print(compressed)

# %%
check_sum(compress2(example))

# %%
print(check_sum(compress2(input_string)))

# %%
