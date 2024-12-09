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
import numpy as np

# %%
example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

# %%
equations = []
for line in example.split("\n"):
    split = line.split(":")
    val = int(split[0])
    elements = split[1].split()
    equations.append([val] + [int(e) for e in elements])

# %%
equations

# %%
