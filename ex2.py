import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('data.csv')
plt.figure(figsize=(12, 6))
for column in df.columns:
    plt.plot(df[column], label=column)
plt.show()


