%config InlineBackend.figure_formats = set(['retina'])

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')

sns.distplot(df['house price'], bins=None, kde=False)
plt.title('Histogram: house price')
plt.show()
