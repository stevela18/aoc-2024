# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3.11
#     language: python
#     name: py311
# ---

# %%
import pandas as pd
import numpy as np
import regex as re

# %%
with open("day3input.txt", "r") as file:
    corrupted_string = file.read()


# %%
def mul(s):
    numbers_string = re.findall(r"\d{1,3}", s)
    numbers = [int(x) for x in numbers_string]
    product = 1
    for n in numbers:
        product = product*n
    return product


# %%
pattern = r"mul\(\d{1,3},\d{1,3}\)"


# %%
def sum_of_products(input_s):
    total = 0
    for i in re.finditer(pattern, input_s):
        s = i.group()
        total += mul(s)
    return total
# sum of all mult commands
print(sum_of_products(corrupted_string))

# %%
test = corrupted_string[:2000]
print(test)

# %%
sum_dos = 0
all_the_dos = re.split(r"do(?!n't)", corrupted_string)
for do in all_the_dos:
    dont_in_dos = re.split(r"don't", do)
    sum_dos += sum_of_products(dont_in_dos[0])
# sum of all the mult commands which follow a do before they follow a don't
print(sum_dos)

# %%
