import shutil
import os

newpath = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-1' 
if not os.path.exists(newpath):
    os.makedirs(newpath)


original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-0/Simple.css'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-1/Simple.css'

shutil.copyfile(original, target)

original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-0/info.html'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-1/info.html'

shutil.copyfile(original, target)

original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-0/forestbridge2.png'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-1/forestbridge2.png'

shutil.copyfile(original, target)
