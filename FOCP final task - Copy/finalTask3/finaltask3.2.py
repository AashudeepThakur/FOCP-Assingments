import random
rand_num = random.randint(1111,9999)
f = open("students.txt")
f1 = open("nextfile.txt", "w")
line_list = f.readlines()
# print(line_list)
for i in line_list:
    # print(i)
    split = i.split(",")  
    # print(split)
    id = split[0].split(" ")[0]
    # print(id)
    fnames = split[0].split(" ")[1].lower()
    # print(fnames)
    lastname = split[1].strip().split(",")[0]
    l_initial = lastname[0].lower()
    # print(l_initial)
    f1.write(f"{id} {l_initial}.{fnames}{rand_num}@poppleton.ac.uk\n")

    # print(f"{id} {l_initial}.{fnames}{rand_num}@poppleton.ac.uk")

    # f1 = open("nextfile.txt", "w")