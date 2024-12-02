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
data = pd.read_csv(
    "./input.txt",
    sep="   ",
    header=None,
    engine="python"
)

# %%
data = np.genfromtxt("input.txt", delimiter="   ", dtype=None, encoding="utf-8")

# %%
distance = np.abs(np.sort(data[:,0]) - np.sort(data[:,1]))

# %%
sum(distance)

# %%
