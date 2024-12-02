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
    sep=" ",
    header=None,
)

# %%
import os

# %%
os.getcwd()

# %%
