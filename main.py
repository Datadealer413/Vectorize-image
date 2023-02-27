import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.colors import rgb2hex
import matplotlib.cm as cm
import matplotlib.colors
from collections import Counter

cmap2 = cm.get_cmap('twilight', 13)
colors1 = []
for i in range(cmap2.N):
    rgb = cmap2(i)[:4]
    colors1.append(rgb2hex(rgb))

# Set style
sns.set(style="whitegrid")
