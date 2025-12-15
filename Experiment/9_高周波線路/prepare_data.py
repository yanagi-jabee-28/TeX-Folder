# -*- coding: utf-8 -*-
"""Prepare and clean data1.csv into a simple CSV usable by pgfplots.
Produces data1_clean.csv with header: x,short,open,matched,half
Also optionally saves a PNG preview plot for quick verification.
"""
import csv
from pathlib import Path
import math

p = Path(__file__).parent
src = p / 'data1.csv'
dst = p / 'data1_clean.csv'

rows = []
with src.open('r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    # collect rows where column 7 (index 6) is numeric
    for r in reader:
        # ensure list is long enough
        if len(r) >= 11:
            x = r[6].strip()
            if x.replace('.', '', 1).replace('-', '', 1).isdigit():
                def tonum(s):
                    s = s.strip()
                    if s == '-' or s == '':
                        return ''
                    try:
                        return float(s)
                    except ValueError:
                        return ''
                short = tonum(r[7])
                openv = tonum(r[8])
                matched = tonum(r[9])
                half = tonum(r[10])
                rows.append([float(x), short, openv, matched, half])

# write cleaned csv
with dst.open('w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x','short','open','matched','half'])
    for r in rows:
        writer.writerow(r)

# optional: generate preview PNG using matplotlib
try:
    import matplotlib.pyplot as plt
    import numpy as np
    data = np.genfromtxt(dst, delimiter=',', names=True, dtype=float)
    fig, axs = plt.subplots(2,2, figsize=(8,6))
    axs = axs.ravel()
    cols = ['short','open','matched','half']
    for i,c in enumerate(cols):
        axs[i].plot(data['x'], data[c], marker='o')
        axs[i].set_xlabel('x (mm)')
        axs[i].set_ylabel(c)
        axs[i].grid(True)
    plt.tight_layout()
    png = p / 'data1_preview.png'
    plt.savefig(png, dpi=150)
    print('Preview saved to', png)
except Exception as e:
    print('Matplotlib preview skipped:', e)

print('Wrote', dst)
