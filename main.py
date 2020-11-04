import os

k = int(input("Welcome to the future !\nThis is the solution to all your social media problems !\tYes, ALL !!\n\nLet's Begin!:\n\n[1] Instagram\n\n[99] Exit !\n\nEnter your choice::\t"))

if k == 1:
    os.system('python ig.py')
# if k == 2:
#     os.system('python tw.py')
if k == 3 :
    os.system('python fb.py')
if k == 4 :
    os.system('python reddit.py')
if k == 5:
    os.system('python yt.py')
if k == 6:
    os.system('python sfy.py')
if k == 7:
    os.system('python gh.py')
if k == 8:
    os.system('python stof.py')
elif k == 99:
    print("Adios")
    exit()