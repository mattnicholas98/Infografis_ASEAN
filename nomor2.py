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
df = pd.read_sql('select country.Name, country.Population from country where country.Region = "Southeast Asia" order by Name asc', con = mydb)
print(df)

plt.figure('Ini grafik nomor 2', figsize=(10, 5))
plt.subplot(111) 

plt.pie(df.Population, labels=df.Name, autopct='%.1f%%')
plt.title('Persentase Penduduk ASEAN')
plt.show()