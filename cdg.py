# This utility will look through the possible folder structure and try to find the folder you're looking for
# CDG = Change Dir Global
import sys
import os

allDirs = []
blacklist = ["Anaconda3", "AppData"]
args = sys.argv
args.pop(0)
query = " ".join(args).strip()

for root, dirs, files in os.walk(os.path.expanduser('~/'), topdown=True):
    # first remove any hidden folders
    dirs[:] = [d for d in dirs if not d[0] == '.']
    # then check if this dir is in the blacklist
    dirs[:] = [d for d in dirs if not d in blacklist]

    # for every dir found, check if it matches query
    for name in dirs:
        if name.lower().strip() == query.lower():
            allDirs.append((name, (os.path.join(root, name))))
        #print(os.path.join(root, name))

# if no match is found, say so
if len(allDirs) == 0:
    print("No Results for: " + query)

# If only one result was found, make a bat file
file = open("temp.bat", "w")
file.write(("start cmd /k cd " + allDirs[0][1]))
file.write("\nexit")
file.close()

# We now have a list of matching files, print it back
for dir in allDirs:
    print(dir[1])

