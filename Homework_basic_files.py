files_list = ['1.txt', '2.txt', '3.txt']
files_ind = {}

for file in files_list:
    with open(file, 'r', encoding='utf8') as f:
        content = f.readlines()
        l = len(content)
        files_ind[l] = [file, content]
sorted_files = dict(sorted(files_ind.items()))
print(sorted_files)

for item in sorted_files:
    a = sorted_files.get(item)[0]
    b = str(item)
    c = sorted_files.get(item)[1]
    print(c)
    with open('common.txt', 'a', encoding='utf8') as new_f:
        new_f.writelines(f"\n{a}\n{b}\n")
        for line in c:
            new_f.write(line)
