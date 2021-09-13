import shutil
import os

newpath = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-3' 
if not os.path.exists(newpath):
    os.makedirs(newpath)


original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/scripts/samplefiles/Simple.css'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-3/Simple.css'

shutil.copyfile(original, target)

original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/scripts/samplefiles/accounts.html'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-3/accounts.html'

shutil.copyfile(original, target)

original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/scripts/samplefiles/forestbridge2.png'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-3/forestbridge2.png'

shutil.copyfile(original, target)

print("Lime Tools")
print("__________")
print("Created a new account directory")
print("Next steps: Edit the directory's account files")
print("Commit to GitHub!")
