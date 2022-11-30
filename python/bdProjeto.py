import pymssql 

conexao = pymssql.connect(
    server='sptrack.database.windows.net', 
     user='sptrackClient',
     password='Sprint2SPTrack', 
     database='SPTrack')  

cursor = conexao.cursor()  

def ListaComportamento(so):
 proc = []

 cursor.execute(f"select arquivos,tipoProcesso from processos where so = '{so}' and tipoProcesso='blacklist';")  
 row = cursor.fetchone()

 while row:  
   proc.append(row)
   row = cursor.fetchone()
   
 return proc
