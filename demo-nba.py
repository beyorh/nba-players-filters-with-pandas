import pandas as pd

df=pd.read_csv("datasets/all_seasons.csv")

result=df.head(10) #first 10 data

result=len(df.index) #length of data

result=df.columns #get to title of data

result=df["age"].mean() #The avarage of the players' age

result=df["age"].max() #The maximum age

result=df["player_name"][df["age"].max()] #The name of the maximum player's age

result=df[(df["age"]>=20) & (df["age"]<=25)].sort_values("age",ascending=False) #between 20 to 25 of players

result=df[df["player_name"]=="John Holland"]["team_abbreviation"].iloc[0]

result=df.groupby("team_abbreviation").mean("age") #all of the team's avarage

result=df.groupby("team_abbreviation").mean("age")["age"] #all of the team's avarage age

result=len(df.groupby("team_abbreviation")) #number of the teams

result=df["team_abbreviation"].value_counts() #we can see that how many players played in each team

result=df[df["player_name"].str.contains("and")]





print(result)


