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

# %%
example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

# %%
import re


# %%
def parse_input(s):
    start = re.search(r"\d\d,", s).start()
    page_ordering_rules = [l.split("|") for l in s[:start].split()]
    updates = [l.split(",") for l in s[start:].split()]
    return (page_ordering_rules, updates)


# %%
page_ordering_rules, updates = parse_input(example)


# %%
def make_rules_dict(page_ordering_rules):
    rules_dict = dict()
    for rule in page_ordering_rules:
        key = rule[0]
        value = rule[1]
        if key in rules_dict.keys():
            rules_dict[key].add(value)
        else:
            rules_dict[key] = set([value])
    return rules_dict


# %%
rules_dict = make_rules_dict(page_ordering_rules)


# %%
def check_update_order(update, rules_dict):
    for i, n in enumerate(update[1:]):
        s = set(update[:(i+1)])
        if n in rules_dict.keys():
            if len(s.intersection(rules_dict[n])):
                return -i
    return True


# %%
def part1(s):
    page_ordering_rules, updates = parse_input(s)
    rules_dict = make_rules_dict(page_ordering_rules)
    
    total = 0
    for update in updates:
        if check_update_order(update, rules_dict)>0:
            midpoint = update[int(len(update)/2)]
            total += int(midpoint)
    return total


# %%
with open("day5input.txt", "r") as file:
    input_string = file.read()

# %%
part1(input_string)

# %%
update = updates[3]
print(update)
for i, n in enumerate(update[1:]):
    s = set(update[:(i+1)])
    if n in rules_dict.keys():
        if len(s.intersection(rules_dict[n]))>0:
            print("intersection", s.intersection(rules_dict[n]))
            fixed_update = update.copy()
            fixed_update[i+1], fixed_update[i] =  fixed_update[i], fixed_update[i+1]


# %%
def fix_update(update, rules_dict):
    fixed_update = update.copy()
    i = check_update_order(fixed_update, rules_dict)
    if i > 0 :
        return fixed_update
    else:
        fixed_update[-i+1], fixed_update[-i] =  fixed_update[-i], fixed_update[-i+1]
        return fix_update(fixed_update, rules_dict)


# %%
def part2(s):
    page_ordering_rules, updates = parse_input(s)
    rules_dict = make_rules_dict(page_ordering_rules)
    
    total = 0
    for update in updates:
        if check_update_order(update, rules_dict)<=0:
            fixed_update = fix_update(update, rules_dict)
            midpoint = fixed_update[int(len(fixed_update)/2)]
            total += int(midpoint)
    return total


# %%
part2(input_string)

# %%
