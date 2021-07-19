import os
print('will create new_dir change to it and print cwd')
print(os.getcwd())
os.mkdir("new_dir")
os.chdir("new_dir")
print(os.getcwd())
