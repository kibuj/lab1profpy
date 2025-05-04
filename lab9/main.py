import os

def reader(filename):
    with open(filename, 'r') as f:
        #print(f"Назва файлу:{f}")
        for line in f:
            pass
            #print(line)

def append_student(filename,pib, score):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{pib} — {score}\n")

def file_finder(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            pass
            #print("знайшов")

def search_student(pib,filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if pib in line:
                print(pib)

def sorted_list_by_score(filename):
    score_list = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for l in lines:
            x = l.split()
            print(x)
            if len(x) >= 5:
                score_list.append(float(x[4]))
            print(sorted(score_list))

reader("file.txt")
append_student("file.txt","Креховецький Богдан Миколайович", 4.3 )
file_finder(".", "file.txt")
search_student("Креховецький Богдан Юрійович", "file.txt")
sorted_list_by_score("file.txt")