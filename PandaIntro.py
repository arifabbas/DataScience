import numpy as np
import pandas as pd

# series 1 dimensional data set
series=pd.Series([12,3,4,np.nan, 'Arif'])
# print(series)

# date range for index
dates=pd.date_range("20241020",periods=6)
# print(dates)
# dataframe building
df=pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A','B','C','D'])
# print(df)

# dataframe using dictionary object

dict={'Name':['Arif','Arshad','Yusuf','Hamida'],'Age':[32,35,65,63],'relation':['Bro1','Bro2','Father','Mother']}
df1=pd.DataFrame(dict)
# print(df1)
# print(df1.dtypes)

# print(df.index)
# print(df.shape)
# print(df.size)
# print(df.info())
# print(df.columns)
# print(df.describe())
# print(df.to_numpy())
# print(df.T)


# print(df.sort_values(by='B'))
# print(df.sort_index(axis=1, ascending=False))

# Actual Data reading
df=pd.read_csv("C:\\Users\\rf219\\OneDrive\\Documents\\Development\\vscode_workspace\\MyPython\\DataScience\\stack-overflow-developer-survey-2024\\survey_results_public.csv")
# print(df.head())

# changing the index to responseId
df.set_index('ResponseId', inplace=True)
# print(df.sort_index(axis=0,ascending=False).head())
# print(df.sort_values(by='YearsCode',ascending=False).head())
# df.reset_index(inplace=True)
# print(df.head())

#Selecting Columns and Rows
# 
# print(df[['CodingActivities','DevType']].head())
# print(df.iloc[[1,2,3,4],['CodingActivities','DevType']])
# print(df.iloc[[1,2,3,4],[33,55]])

df.rename(columns={'CodingActivities':'Activities'}, inplace=True)

# print(df['Activities'].head())
# print(df['Activities'].replace('Hobby','Free timer'))


# Using Apply function on Series and Dataframe
# def updateCountry(DevType):
#     return str(DevType).upper()
# df['DevType']=df['DevType'].apply(updateCountry)

df['DevType']=df['DevType'].apply(lambda x: str(x).lower())
# print(df['DevType'].head())

df1=df[['JobSatPoints_1','JobSatPoints_4']]
# print(df1.head())
# df1=df1.apply(pd.Series.max)
# print(df1.head())
# df1=df1['JobSatPoints_1'].replace({np.nan: 0})
# print(df1.head())

print(df.drop(columns=['MainBranch','Age']))
df = pd.concat([df, pd.DataFrame.from_records([{ 'Checks': 'Tony'}])])
print(df.tail())
df.drop(index=[1,2,3,4], inplace=True)
print(df.head())