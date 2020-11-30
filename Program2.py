# -*- coding: utf-8 -*-
"""
Program #2

Grading ID: D9744

This program will take a list of students responses to cafeteria food and 
perform analysis on them out put that analysis.

Also will display visual chart of the student response data.
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statistics as stat

student_resp = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

values, freqs = np.unique(student_resp, return_counts=True)
# print(values, freqs)

print(f'Minimum = {min(student_resp)}')
print(f'Maximum = {max(student_resp)}')
print(f'Range = {min(student_resp)} , {max(student_resp)} ')
print(f'Mean = {stat.mean(student_resp)}')
print(f'Median = {stat.median(student_resp)}')
print(f'Mode = {stat.mode(student_resp)}')
print(f'Variance = {stat.variance(student_resp)}')
print(f'Standard Deviation = {stat.stdev(student_resp)}')

title = f'{len(student_resp):,} Students Surveyed'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=freqs, palette='mako')
axes.set_title(title)
axes.set(xlabel= 'Values', ylabel= 'Frequency')
axes.set_ylim(top=max(freqs) * 1.15)
for bar, freq in zip(axes.patches, freqs):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{freq:,}\n{freq / len(student_resp):.3%}'
    axes.text(text_x, text_y, text,
              fontsize=11, ha='center', va='bottom')
