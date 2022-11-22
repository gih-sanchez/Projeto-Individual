import bdProjeto
from  platform import system
from subprocess import check_output
from numpy import array

if(system() == "Windows"):

  output = check_output("TASKLIST /NH /FO TABLE | SORT /R /+68'",shell=True)
else:
   output = check_output( "top -b -n 2 | sed -n '8, 12p' ",shell=True)

output = array(output.split(), dtype='<U')

print(output)
