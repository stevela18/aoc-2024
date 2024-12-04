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
import numpy as np
import re

# %%
test = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


# %%
def s_to_array(s, alt=False):
    if alt:
        s_array = np.array([list(x[::-1]) for x in s.split()])
    else:
        s_array = np.array([list(x) for x in s.split()])
    return(s_array)


# %% [markdown]
# # PART 1

# %%
re.findall(r"XMAS", test) + re.findall(r"SAMX", test)


# %%
def transpose(s_array):
    s_output = ""
    for j in range(s_array.shape[1]):
        for i in range(s_array.shape[0]):
            s_output += s_array[i,j]
        s_output += "\n"
    return s_output


# %%
def rotate_45(s_array):
    s_output = []
    for j in range(s_array.shape[1]):
        for i in range(s_array.shape[0]):
            if len(s_output) == i+j:
                s_output.append(str(s_array[i,j]))
            else:
                s_output[i+j] += s_array[i,j]
    return "\n".join(s_output)


# %%
abc = "ABCD\nEFGH\nIJKL\nMNOP\nQRST\n"

# %%
print(abc)
print(transpose(s_to_array(abc)))
print(rotate_45(s_to_array(abc)))
print(rotate_45(s_to_array(abc, True)))

# %%
with open("day4input.txt", "r") as file:
    crossword = file.read()

# %%
for i in range(4, -1, -1):
    print(i)


# %%
def count_crossword(crossword):
    s_array = s_to_array(crossword)
    crossword_t = transpose(s_array)
    crossword_r = rotate_45(s_array)
    s_array_alt = s_to_array(crossword, True)
    crossword_r2 = rotate_45(s_array_alt)
    count = len(
        re.findall(r"XMAS", crossword) + 
        re.findall(r"SAMX", crossword) + 
        re.findall(r"XMAS", crossword_t) + 
        re.findall(r"SAMX", crossword_t) + 
        re.findall(r"XMAS", crossword_r) + 
        re.findall(r"SAMX", crossword_r) +
        re.findall(r"XMAS", crossword_r2) + 
        re.findall(r"SAMX", crossword_r2)
    )
    return count


# %%
count_crossword(test)

# %%
count_crossword(crossword)

# %% [markdown]
# # Part 2

# %%
s = test
s_array = np.array([list(x) for x in s.split()])


# %%
def check_for_x_mas(a):
    diag_1 = ""
    diag_2 = ""
    for i in range(3):
        diag_1 += a[i,i]
        diag_2 += a[i,2-i]
    return ((diag_1=="MAS")|(diag_1=="SAM"))&((diag_2=="MAS")|(diag_2=="SAM"))


# %%
def find_X_mas(s):
    count = 0
    s_array = np.array([list(x) for x in s.split()])
    for i in range(1, s_array.shape[0]-1):
        for j in range(1, s_array.shape[1]-1):
            if s_array[i,j] == "A":
                a = s_array[(i-1):(i+2),(j-1):(j+2)]
                count += check_for_x_mas(a)
    return count


# %%
find_X_mas(crossword)

# %%
