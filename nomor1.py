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

# give out various colors
warna = ['r', 'orange', 'y', 'g', 'b', 'k', 'pink', 'violet', 'r', 'y', 'orange']
plt.style.use('seaborn')

plt.figure('Ini grafik nomor 1', figsize=(10, 5))
plt.subplot(111) 

# plot the bar graph
plt.bar(df.Name, df.Population, color=warna)
plt.title('Populasi Negara ASEAN')
plt.xlabel('Negara')
plt.ylabel('Populasi (x100jt jiwa)')
plt.xticks(rotation = 45)
plt.grid(True)
plt.tight_layout()

for i, j in enumerate(df.Population):
    plt.text(i-.4, j, str(j), color='k')

plt.show()