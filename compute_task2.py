# %%
# Importing all the necessary packages
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use("ggplot")
pd.options.display.max_columns = 200
pd.options.display.max_rows = 19000
pd.options.display.max_seq_items




# %% [markdown]
# # Understanding data

# %%
df = pd.read_csv("C:/Users/Nitish B. Singh/Downloads/data.csv")         # Reads the specified csv file
df.shape            # Gives the number of rows and columns in the data

# %% [markdown]
# <!-- Understanding the data -->

# %%
df.head()           # Prints the first 5 rows of the data

# %%
df.tail()           # Prints the last 5 rows of the data

# %%
df.columns          # Prints all the columns in the data

# %%
df.dtypes           # Prints the datatypes of the values in the dataframe

# %%
df.describe()           # Summarizes the whole dataframe

# %% [markdown]
# # Data Preparation

# %%
df = pd.read_csv("C:/Users/Nitish B. Singh/Downloads/data.csv")
df = df[['sofifa_id', 'player_url', 'long_name',                    # Filters out and gives the dataframe with only the specified columns, making the data easier to understand
           'age', 'joined','overall',
       'height_cm', 'weight_kg', 'nationality', 'club_name',
       'international_reputation','movement_sprint_speed',
       
       ]].copy()


# %%
df.dtypes

# %%
pd.to_datetime(df["joined"])            # Changes datatype from object to datetime

# %%
df.columns

# %% [markdown]
# 

# %%
df = df.rename(columns={'sofifa_id':'Sofifa_ID',
                        'player_url':'Player_URL',
                        'long_name':'Long_Name',
                        'height_cm':'Height_cm',
                        'weight_kg':'Weight_kg',
                        'age':'Age','nationality':'Nationality',                    # Renaming the column names to make it look more appealing
                        'club_name':'Club_Name',
                        'international_reputation':'International_Reputation',
                        'movement_sprint_speed':'Sprint_speed',
                        'joined':'Date_joined',
                        'overall':'Overall_Rating'
                        })

# %%
df.head()

# %% [markdown]
# # Data Cleaning

# %%
df.isna().sum()             # Gives the count of the rows which have empty values for each column 

# %%
df = df.loc[~df['Club_Name'].isna()]  \
        .reset_index(drop=True)                # Removes the rows which are NA


# %%
df.loc[df.duplicated()]         # prints the duplicate rows

# %% [markdown]
# Since there are no duplicate rows found, we can move further to plotting out dataframe

# %%
df.shape

# %% [markdown]
# # Plots

# %%
ax = df['Overall_Rating'].value_counts() \
.head(10)   \
.plot(kind='bar',title='Top rating')
ax.set_xlabel('Overall_Rating')
ax.set_ylabel('Count')

# %%
a = df['Sprint_speed'].plot(kind="hist",bins = 20,title="Movement sprint speed")
a.set_xlabel("Sprint_speed")

# %% [markdown]
# Now, checking the height vs weight of players which showws the body mass index describing the fitness of the players

# %%
df.plot(kind="scatter",x="Weight_kg",y = "Height_cm",title="Height vs Weight" )
plt.show()

# %% [markdown]
# With respect to age

# %%
sns.scatterplot(x="Weight_kg",y = "Height_cm",data = df, hue = 'Age')
plt.show()

# %%
df.columns

# %% [markdown]
# # Feature relationship

# %%
sns.pairplot(data = df,vars=['International_Reputation', 'Sprint_speed',
                             'Overall_Rating', 'Height_cm', 'Weight_kg'],hue = 'Age')
plt.show()

# %% [markdown]
# This shows the graphs between different features of the dataframe which can help us understand about the relationship between the features. It also helps in detection of outliers if there are any.

# %% [markdown]
# Here, we can see an outlier in the height vs weight graph

# %% [markdown]
# # Which countries have the most players with highest overall ratings ?

# %%
df['Nationality'].value_counts()

# %%
ax = df.groupby('Nationality')['Overall_Rating']   \
.agg(['mean','count'])  \
.query('count >= 400')   \
.sort_values('mean')['mean']    \
.plot(kind="barh",title="Average rating of players in countries")
ax.set_xlabel("Average rating of players")
ax.set_ylabel("Nationality")
plt.show()

# %% [markdown]
# Here, we can see that Brazil has the most players with good overall rating.
# Also, a huge population of players in fifa21 belong to the countries like England, Germany and Spain.
