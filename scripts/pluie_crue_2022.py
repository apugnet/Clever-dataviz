import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

current_path =  os.path.dirname(__file__)
data = pd.read_csv(current_path + "/pluie_crue_2022.csv")
sns.catplot(data=data.sort_values("date_observation"), x="date_observation", y='precipitation', hue="distance")

plt.show();
