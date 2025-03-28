import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import warnings
import statsmodels
import seaborn as sns
import matplotlib.pylab as plt
from scipy import stats
warnings.filterwarnings('ignore')
matplotlib.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
# Load the data
'''
Blouses Pants
Casual bottoms Shorts
Chemises Skirts
Dresses Sleep
Fine gauge Sweaters
Intimates Swim
Jackets Trend
Jeans
Knits
Layering
Legwear
Lounge
Outerwear
'''
df = pd.read_excel('total.xlsx')
# Check the first few rows of the dataframe to understand its structure
df.head()
# Convert scores to categories
categories = {'积极': lambda x: x > 0, '中性': lambda x: x == 0, '消极': lambda x: x < 0}
# Apply the transformation for each topic
for topic in ['topic1', 'topic2', 'topic3', 'topic4']:
    df[topic] = df[topic].apply(lambda x: next((key for key, func in categories.items() if
func(x)), None))
# Check the transformation
df.head()
import matplotlib.pyplot as plt
# Create a figure for the pie charts
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
axes = axes.flatten() # Flatten the axes array for easy iteration
topics = ['topic1', 'topic2', 'topic3', 'topic4']
for ax, topic in zip(axes, topics):
    # Count the frequency of each category in the current topic
    counts = df[topic].value_counts()
    # Plot pie chart
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    ax.set_title(f'Topic {topic[-1]} Distribution')
    plt.tight_layout()
    plt.show()