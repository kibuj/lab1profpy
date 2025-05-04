
def file_sorter(filename, file1, file2):
    iter = True
    with open(filename, "r", encoding="utf-8") as f, \
        open(file1, "a", encoding="utf-8") as file1, \
        open(file2, "a", encoding="utf-8") as file2:
        lines = f.readlines()
        for l in lines:
            print(l)
            if iter:

                    file1.write(l)
                    iter = False
            if not iter:

                    file2.write(l)
                    iter = True

file_sorter('file.txt',"file1.txt","file2.txt")