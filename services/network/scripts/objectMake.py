import shutil
import os

newpath = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-2' 
if not os.path.exists(newpath):
    os.makedirs(newpath)


original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/scripts/samplefiles/Simple.css'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-2/Simple.css'

shutil.copyfile(original, target)

original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/scripts/samplefiles/info.html'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-2/info.html'

shutil.copyfile(original, target)

original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/scripts/samplefiles/object.html'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-2/object.html'

shutil.copyfile(original, target)

original = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/scripts/samplefiles/forestbridge2.png'
target = r'/Users/ariel/Documents/Developer/Web Projects/Lime/services/network/per/usr-2/forestbridge2.png'

shutil.copyfile(original, target)

print("Lime Tools")
print("__________")
print("Created a new object directory")
print("Next steps: Edit the directory's info and object files")
print("Commit to GitHub!")
