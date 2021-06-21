import shutil
import os

newpath = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-2' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-0/wallet1.html'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-2/wallet1.html'

shutil.copyfile(original, target)

original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-0/Simple.css'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-2/Simple.css'

shutil.copyfile(original, target)

original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-0/accounts.html'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-2/accounts.html'

shutil.copyfile(original, target)

original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-0/info.html'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-2/info.html'

shutil.copyfile(original, target)

original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-0/forestbridge2.png'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-2/forestbridge2.png'

shutil.copyfile(original, target)