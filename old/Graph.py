import inline
import matplotlib
import numpy as np
import pandas as pd
import inline
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.lines as mlines
import warnings; warnings.filterwarnings(action='once')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17]
y = [1, 1, 2, 3, 3, 5, 5, 8, 9, 6, 9, 9, 11, 11, 17]
week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', "суббота", "воскресенье"]
x1 = [11.1, 12.13, 12.5, 13.6, 14, 16.3, 17]
y1 = [1, 2, 3, 4, 5, 6, 7]

from pandas.plotting import parallel_coordinates

# Import Data
df_final = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/diamonds_filter.csv")

# Plot
plt.figure(figsize=(12,9), dpi= 80)
parallel_coordinates(df_final, 'cut', colormap='Dark2')

# Lighten borders
plt.gca().spines["top"].set_alpha(0)
plt.gca().spines["bottom"].set_alpha(.3)
plt.gca().spines["right"].set_alpha(0)
plt.gca().spines["left"].set_alpha(.3)

plt.title('Parallel Coordinated of Diamonds', fontsize=22)
plt.grid(alpha=0.3)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# if __name__ == '__main__':
#     a = 1