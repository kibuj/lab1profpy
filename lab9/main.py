def reader(filename):
    with open(filename, 'r') as f:
        print(f"Назва файлу:{f}")
        for line in f:
            print(line)

reader("file.txt")