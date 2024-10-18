from mysql.connector import connect, Error
import datetime
import matplotlib.pyplot as plt 

try:
 
    # define a connection object
    conn = connect(user='root', password='**********',
                host='127.0.0.1',
                database='personal')
 
    # open cursor, define and run query, fetch results
    cursor = conn.cursor()
    query = 'SELECT transac_id, price, date, time, transac_type, consumer_id FROM consumption;'
    cursor.execute(query)
    result = cursor.fetchall()
 
    # close the cursor and database connection
    cursor.close()
    conn.close()

# catch exception and print error message
except Error as err:
  print('Error message: ' + err.msg)

conn.close()

# make lists of all columns
transac_id_lst = []
price_lst = []
datetime_lst = []
time_lst = []
transac_type_lst = []
consumer_id_lst = []
for r in result:
    transac_id_lst.append(r[0])
    price_lst.append(float(r[1]))
    datetime_lst.append(r[2])
    time_lst.append(r[3])
    transac_type_lst.append(r[4])
    consumer_id_lst.append(r[5])
print(datetime_lst)

fig, ax = plt.subplots()
ax.scatter(datetime_lst, price_lst)
ax.set_xlabel("Date (yyyy-mm-dd)")
ax.set_ylabel("Transaction amount (US$)")
plt.show()
