import sys,os
# on fait le activate avant de lancer apache car sinon il trouve pas python 3.4 car sur mon PC default = 2.7
# #activate_this = R'D:\dev\_Client\LOV\EcoTaxa\Python\Scripts\activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))
#exec(open(activate_this).read())


# sys.path.insert(0, R'D:\dev\_Client\LOV\EcoTaxa\EcoTaxa')
sys.path.insert(0,os.path.normpath(os.path.dirname(os.path.realpath(__file__))))
os.chdir(os.path.normpath(os.path.dirname(os.path.realpath(__file__))))
# sys.path.insert(0, R'D:\dev\_Client\LOV\EcoTaxa\Python\Lib\site-packages')
sys.path.insert(0,os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), R"..\Python\Lib\site-packages")))
# sys.path.insert(0, R'D:\dev\_Client\LOV\EcoTaxa\Python\Lib\site-packages\psycopg2-2.6-py3.4-win32.egg')
sys.path.insert(0,os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), R"..\Python\Lib\site-packages\psycopg2-2.6-py3.4-win32.egg")))
from appli import app as application

if sys.platform.startswith('win32'):
    application.PythonExecutable=os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), R"..\Python\Scripts\python.exe"))
else:
    application.PythonExecutable='/usr/local/bin/python3'
