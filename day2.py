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
import pandas as pd
import numpy as np

# %%
data = []
with open("day2input.txt", "r") as file:
    for line in file:
        d = np.array(line.strip().split(" "), dtype=int)
        data.append(d)


# %%
def is_increasing(a):
    flag = True
    i = 0
    i_max = len(a)-2
    result = False
    while flag:
        if a[i+1] <= a[i]:
            flag = False
        elif (i==i_max):
            flag = False
            result = True
        i += 1
    return result
def is_decreasing(a):
    a_reversed = a[::-1]
    return is_increasing(a_reversed)
def safe_difference(a):
    flag = True
    i = 0
    i_max = len(a)-2
    result = False
    while flag:
        diff = np.abs(a[i+1] - a[i])
        if (diff<1)|(diff>3):
            flag = False
        elif (i==i_max):
            flag = False
            result=True
        i += 1
    return result
        
    
def safe_report(a):
    result = (is_increasing(a) | is_decreasing(a)) & safe_difference(a)
    return result


# %%
# number of safe reports
sum([safe_report(d) for d in data])


# %%
def safe_report_dampener(a):
    result = False
    flag = True
    if safe_report(a):
        result = True
    else:
        i = 0
        i_max = len(a)-1
        while flag:
            test_a = np.delete(a, i)
            if safe_report(test_a):
                flag = False
                result = True
            elif i==i_max:
                flag = False
            i +=1
    return result


# %%
# number of safe reports with dampener
sum([safe_report_dampener(d) for d in data])

# %%
