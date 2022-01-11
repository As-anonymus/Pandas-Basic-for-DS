#!/usr/bin/env python
# coding: utf-8

# # Reading & Writing

# In[2]:


import pandas as pd
#for reading file data
df = pd.read_csv(r"C:\Users\Aditya Singh\Documents\Book1.csv")
#df = pd.read_excel("Book1.xlsx","Sheet1")
df


# In[3]:


import pandas as pd
#header = none , names =['ticker','eps','revenue','price','people']...for mising header
#nrows = 3...for limiting lines read
na_values=['not available','n.a.']#...for cleaning & munging & wrangling...use dictionary for specifying instead of list
df = pd.read_csv(r"C:\Users\Aditya Singh\Documents\Book2.csv",header=1,na_values={'eps':['not available','n.a.'],
                                                                               'revenue':['not available','n.a.',-1],
                                                                                 'people':['not available','n.a.']})
df


# In[ ]:


#To Write
columns =['tickers','eps']...for slective column
#header = False...for no header
df.to_csv('new.csv',index=False)


# # Handling Missing Data

# In[142]:


import pandas as pd
df = pd.read_csv(r"C:\Users\Aditya Singh\Documents\Book3.csv",parse_dates=['day'])
df.set_index('day',inplace=True)
df


# In[143]:


new_df=df.fillna({'event':'no-event',
                 'windspeed':0,
                 'temperature':0})
new_df


# In[138]:


#bfill...to fill prev value
#axis = ...method of copying

new_df = df.fillna(method="ffill",limit=1)
new_df


# In[139]:


new_df = df.interpolate(method="time")
new_df


# In[140]:


#thresh=1...with at leasy one valid value
new_df = df.dropna(how="all")
new_df


# In[141]:


#for inserting missing range
dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)
df


# # Dealing with special values

# In[44]:


import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\Aditya Singh\Documents\Book4.csv")
df


# In[50]:


#can pass replacing values as list
new_df = df.replace({'temperature':-99999,
                    'windspeed':-99999,'event':'0'
                    },np.NaN)
new_df


# In[52]:


new_df = df.replace({-99999:np.NaN,
                    '0':'Sunny'})
new_df


# In[56]:


#Regex Tut
#To replace full list replace by another list
new_df = df.replace({
    'temperature': '[A-Za-z]',
    'windspeed':'[A-Za-z]',
},'',regex=True)
new_df = df.replace({
                    '0':'Sunny'})
new_df


# # Split,Apply,Combine

# In[3]:


#  import pandas as pd
#  df = pd.read_csv(r"C:\Users\Aditya Singh\Documents\Book5.csv")
#  df


# In[4]:


# g = df.groupby('city')
# g


# In[5]:


# for city,city_df in g:
#     print(city)
#     print(city_df)


# In[6]:


# g.get_group('mumbai')


# In[7]:


# g.max()


# In[8]:


# g.mean()


# In[9]:


# g.describe()


# In[10]:


# %matplotlib inline
# g.plot()


# # Concating DataFrames

# In[12]:


import pandas as pd
india_weather = pd.DataFrame({
"city":["mumbai","delhi","banglore"],
   "temperature": [32,45,30],
   "humidity":[80,60,78]}
)
india_weather


# In[13]:


import pandas as pd
us_weather = pd.DataFrame({
"city":["new york","chicago","orlandoo"],
   "temperature": [22,35,10],
   "humidity":[60,90,48]}
)
us_weather


# In[16]:


df =  pd.concat([india_weather,us_weather],ignore_index=True)
df


# In[17]:


#if you want third pass axis = 1 amd index =[1,0]
df =  pd.concat([india_weather,us_weather],
                #ignore_index=True,
                keys=["india","us"])
df


# # Merging Dataframes

# In[23]:


import pandas as pd
df1 = pd.DataFrame({
"city":["new york","chicago","baltimore","orlando"],
    "temperature": [22,35,77,10] }
)
df1


# In[24]:


import pandas as pd
df2 = pd.DataFrame({
"city":["new york","chicago","san frasico"],
   
    "humidity":[60,90,48]}
)
df2


# In[27]:


#it performs intersection,so for union
#to know the details data frame
#if same column use suffixes=("","")...to name thwm
df3 =pd.merge(df1,df2,on="city",how="outer",indicator="True")
df3


# # Pivot Table

# In[34]:


import pandas as pd
df = pd.read_csv(r"C:\Users\Aditya Singh\Documents\Book6.csv")
df


# In[37]:


#index...x...columns...y...values...only output data
df.pivot(index='date',columns='city',values='humidity')


# In[38]:


import pandas as pd
df = pd.read_csv(r"C:\Users\Aditya Singh\Documents\Book7.csv")
df


# In[40]:


#if similar values for a key pivot_table takes average...aggfunc
#margins give total/aggregate
df.pivot_table(index='city',columns='date',aggfunc="sum",margins=True)


# In[42]:


df = pd.read_csv(r"C:\Users\Aditya Singh\Documents\Book8.csv")
df


# In[44]:


#string to date conversion
df['date']=pd.to_datetime(df['date'])
df


# In[45]:


#Grouper function
df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city')


# # Reshaping Dataframe using Melt

# In[50]:


import pandas as pd
df = pd.read_csv(r"C:\Users\Aditya Singh\Documents\Book9.csv")
df


# In[53]:


#id vars ... not melted
df1=pd.melt(df,id_vars=["day"],var_name="city",value_name="temp")
df1#[df1["variable"]=="chicago"]...for specific


# # Stacking & Unstacking

# In[131]:


import pandas as pd
df = pd.read_excel(r"C:\Users\Aditya Singh\Documents\Book10.xlsx",header=[0,1],index_col=[0])


df


# In[133]:


df_stacked=df.stack(dropna=True)
df_stacked


# In[80]:


df_stacked.unstack()


# # Crosstab

# In[5]:


get_ipython().run_cell_magic('HTML', '', '<style type="text/css">\n    table.dataframe td, table.dataframe th {\n        border: 1px solid gray;\n    }\n</style>')


# In[7]:


import pandas as pd
df = pd.read_csv(r"C:\Users\Aditya Singh\Documents\Book11.csv")
df


# 
# pd.crosstab(df.Nationality,df.Handeness)#values=df.Age,aggfunc=np.average

# In[13]:


#shift + tab....normalize='index'...for percentage
pd.crosstab(df.Sex,[df.Handeness,df.Nationality],margins=True)


# # Time series analysis 

# In[60]:


import pandas as pd
import warnings
warnings.filterwarnings('ignore')
#the prev Date column was string so we use parse to convert it
#then we replaced deafault index by date time
df = pd.read_csv(r"C:\Users\Aditya Singh\Downloads\HistoricalData_1641821692395.csv",parse_dates=["Date"],index_col="Date")
df.head(5)


# In[61]:



charti = df['Close']
for i in range(len(charti)):
    charti[i]=charti[i].replace('$','')
#print(charti)
df['Close']=charti
df.head(5)


# In[66]:


df['Close']=pd.to_numeric(df['Close'])


# In[64]:


type(df['Volume'])


# In[44]:


df.index


# In[30]:


df["2021-07":"2021-03"].Volume.mean()


# In[70]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.resample('Q').mean().plot(kind='bar')


# In[71]:


df.Close.plot()
#without resampling the graph is way too granualar


# In[74]:


#For Missing Dates Column
import pandas as pd
df = pd.read_csv(r"C:\Users\Aditya Singh\Downloads\HistoricalData_1641821692395_2.csv")
df.head()


# In[110]:


charti = df['Close']
for i in range(len(charti)):
    charti[i]=charti[i].replace('$','')
#print(charti)
df['Close']=charti
df.head(5)
df['Close']=pd.to_numeric(df['Close'])


# In[107]:


#if dont know end... 
#rng = pd.date_range(start="5/1/2021",periods=252,freq='B')
#doesnt handle holidays specific to calender
rng = pd.date_range(start="5/1/2021",end="4/19/2022",freq='B')
rng


# In[111]:


df.set_index(rng,inplace=True)
df


# In[ ]:





# In[112]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.plot()


# In[113]:


df["2021-05-03":"2021-08-03"].Close.mean()


# In[114]:


#helps regenerte data frame acc to new freq
#pad helps carry forward the prices/data similar to fill na
df.asfreq('D',method='pad')


# In[118]:


import numpy as np
#pd.to_datetime(dates)....pd.to_datetime('5$12$2020',format='%d$%m$%Y')

ts = pd.Series(np.random.randint(1,10,len(rng)),index =rng)
ts.head(10)
#len(rng)


# In[1]:


#Time Period
# provide freq argument = 'M'...for monthly 
import pandas as pd
y = pd.Period('2016')
y


# In[2]:


dir(y)#y.start_time


# In[5]:


d = pd.Period('2016-02-28')
d


# In[6]:


d+1


# In[7]:


#quarterly tp
q = pd.Period('2017Q1',freq ='Q-JAN')
q


# In[8]:


q.start_time


# In[9]:


q.asfreq('M',how="start")


# In[14]:


idx = pd.period_range('2011','2017',freq='Q-JAN')
idx


# In[15]:


idx[0].start_time


# In[16]:


idx[0].end_time


# In[18]:


import numpy as np
ps =pd.Series(np.random.randn(len(idx)),idx)
ps


# In[19]:


ps.index


# In[ ]:




