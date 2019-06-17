import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# connect to mysql
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'Matthew',
    password = 'Matthew1998',
    database = 'world'
)

# read the data
df = pd.read_sql('select country.Name, country.SurfaceArea from country where country.Region = "Southeast Asia" order by Name asc', con = mydb)
print(df)

plt.figure('Ini grafik nomor 4', figsize=(10, 5))
plt.subplot(111) 

plt.pie(df.SurfaceArea, labels=df.Name, autopct='%.1f%%')
plt.title('Persentase Luas Daratan ASEAN')
plt.show()