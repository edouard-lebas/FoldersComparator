from os import listdir, path
from os.path import isfile, join
folder1 = input("Full path of folder 1 (c:\\users...) > ")
folder2 = input("Full path of folder 2 (c:\\users...) > ")

if path.isdir(folder1):
    print("Folder 1 is a valid path")
else:
    exit("Folder 1 must be a valid path. You entered "+folder1)

if path.isdir(folder2):
    print("Folder 2 is a valid path")
else:
    exit("Folder 2 must be a valid path. You entered "+folder2)



folder1_files = [f for f in listdir(folder1) if isfile(join(folder1, f))]
folder2_files = [f for f in listdir(folder2) if isfile(join(folder2, f))]

folder1_files = set(folder1_files)
folder2_files = set(folder2_files)

in_two_folders = folder1_files.intersection(folder2_files)
only_in_one_folder = folder1_files.union(folder2_files) - in_two_folders

print ("\n-------- "+str(len(in_two_folders))+" Files in the two folders --------")
for a in in_two_folders:
    f1_a = join(folder1, a)
    f2_a = join(folder2, a)
    if isfile(f1_a):
        print(f1_a)
    else:
        print(f2_a)

print ("\n-------- "+str(len(only_in_one_folder))+" Files only in one folder --------")
for b in only_in_one_folder:
    f1_b = join(folder1, b)
    f2_b = join(folder2, b)
    if isfile(f1_b):
        print(f1_b)
    else:
        print(f2_b)
