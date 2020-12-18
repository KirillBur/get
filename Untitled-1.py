import pathlib
import shutil
import os
import requests
path = str(pathlib.Path().absolute())+ '\\icons'
print(path)

try:
    shutil.rmtree(path)
except OSError :
    print ("Deletion  of the  directory %s failed" % path)
else:
    print ("Successfully deleted  the  directory %s" % path)

try:
    os.mkdir(path)
except OSError :
    print("Creation  of the directory %s failed" % path)
else:
    print ("Successfully deleted  the  directory %s" % path)

names = [
'python',
'c-plus-plus-logo',
'c-sharp-logo'
]
iconSize= 50 
IconTheme= 'ios'
colors = {'blue': '005EB8','orange': 'FF9919'}
for key in colors:

    colorPath=path + '\\' + key

    try:
        os.mkdir(colorPath)
    except OSError :
        print("Creation  of the directory %s failed" % colorPath)
    else:
        print ("Successfully deleted  the  directory %s" % colorPath)
    for n in  names :
        name = n + '.png' 
        r= requests.get('https://img.icons8.com/' + IconTheme + '/' + colors[key] + '/' + str(iconSize) + '/' + name, allow_redirects=True)
        open(colorPath + '/' + name, 'wb').write(r.content)   
