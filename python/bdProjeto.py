import pymssql 
conexao = pymssql.connect(
    server='sptrack.database.windows.net', 
   user='sptrackClient',
     password='Sprint2SPTrack', 
     database='SPTrack')  

cursor = conexao.cursor()  

def check_vuneravel(so):
 cursor.execute(f'select arquivos from Table where so = {so};')  
 row = cursor.fetchone()  
 while row:  
  print(row[0])
  row = cursor.fetchone()  
