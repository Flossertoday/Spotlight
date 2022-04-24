import os
assets = os.path.expanduser('~/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets')
picture = os.path.expanduser('~/Pictures')
spotlight = os.path.expanduser('~/Pictures/Spotlight')

if not('Spotlight' in os.listdir(picture)):
    os.mkdir(spotlight)
else:
    print('\'Spotlight\' exists')

list0 = os.listdir(assets)
list1 = os.listdir(spotlight)

for fileN in list0:
    if not(fileN in list1):
        f = open(assets+'/'+fileN, 'rb')
        cop = f.read()
        f.close

        f2 = open(spotlight+'/'+fileN+'.jpg', 'wb')
        f2.write(cop)
        f2.close
    else:
        print('WRONG WAY')

print('DONE. Check \'~/Picture/Spotlight\'')