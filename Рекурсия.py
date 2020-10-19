from os import walk

def rec(dir):
    for (somth, dirnames, files) in walk(dir):
        for file in files:
            print(file)
        if len(dirnames) != 0:
            for i in range(len(dirnames)):
                rec(dir + '\\' + dirnames[i])
        return 0
rec("dz_3")
