import urllib.request, urllib.parse, urllib.error
import ssl
import sqlite3
dbname=input('enter database name without extenation :')

connection=sqlite3.connect(dbname+'.sqlite')
query=connection.cursor()
while True:
 data1=input('enter table name or type quit for break program::')
 if data1=='quit':break
 elif data1.startswith('create') or data1.startswith('CREATE'):
  try:
   query.execute(data1)
   print('table is created')
  except:
   print('sintex error')
   continue

 elif data1.startswith('insert ') or data1.startswith('INSERT '):
  try:
   query.execute(data1)
   connection.commit()
   print('data is inserted')
  except:
   print('query sintex error')
   continue
 elif data1.startswith('select ') or data1.startswith('SELECT '):
  try:
   query.execute(data1)
   for rows in query:
    print(rows)
  except:
   print('select query sintex error')
   continue
 elif data1.startswith('update ') or data1.startswith('UPDATE '):
  try:
   query.execute(data1)
   connection.commit()
   print('data is updated successfuly')
  except:
   print('update query sintex error')
   continue
 elif data1.startswith('delete ') or data1.startswith(' DELETE '):
  try:
   query.execute(data1)
   connection.commit()
   print('data is deleted')
  except:
   print(' delete query sintex error')
   continue
 elif data1.startswith('drop ') or data1.startswith('DROP '):
  try:
   query.execute(data1)
   connection.commit()
   print('droped successfuly')
  except:
   print('drop query sintex error')
   continue
 elif data1.startswith('show ') or data1.startswith('SHOW '):
  try:
   query.execute(data1)
   for tables in query:
    print(tables)
  except:
   print('show  query sintex error')
   continue
 else:
  print('something is rong try again')
  continue
print('bai bai user')