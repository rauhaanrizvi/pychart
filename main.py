import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size=100)
y = np.random.normal(size=100)

sns.boxplot(x=x, color = 'g')
plt.savefig('output/box.png')