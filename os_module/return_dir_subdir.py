import os
os.listdir("scripts") # file that we will be reading
dir = "scripts"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)#using os.path.join, we join the directory to each of those file names and create a String with a valid full name. 
    if os.path.isdir(fullname):
        print("{} is a DIR".format(fullname))
    else:
         print("{} is a FILE".format(fullname))

"""What's the purpose of the os.path.join function?


It creates a string containing cross-platform concatenated directories."""