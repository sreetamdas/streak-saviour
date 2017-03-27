import os, datetime
from Tkinter import Tk
from tkFileDialog import askdirectory


Tk().withdraw()
directory = askdirectory()

print(directory)

os.system('cd ' + directory)
date = datetime.date.today()
date = date.strftime('%b %d, %Y')
print date

os.system('echo `' + date + '` >> README.md')
