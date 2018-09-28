import os, sys

f = []


# Set the directory you want to start from
scriptPath = sys.path[0]
rootDir = "C:/Users/Christian/Desktop/witheredgryphon github/witheredgryphon.github.io/sites/vn_temp/"
for scriptPath, subdirs, files in os.walk(rootDir):
    for name in files:
        f.append(os.path.join(scriptPath, name))
		
text = open("test.txt", "w")
for i in f:
	text.write(i + '\n')
	
print('done')