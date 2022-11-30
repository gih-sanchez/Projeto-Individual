import bdProjeto
from  platform import system
from psutil import process_iter
import os,time

rest = bdProjeto.ListaComportamento(system())

while True:
 
 for proc in process_iter() :

  try:
   if rest[1][0] in proc.name():
     os.system(f" taskkill /PID {proc.pid} /F ")
  
  except:
      pass

 time.sleep(3) 