data = []

top_3 = [0]
top_3_sum = 0
elf_sum = 0



with open("input/Day1.txt", "r") as f:
    for line in f:
        data.append(line.strip())
        

for el in data:
    if (str(el) == ''):
        for elf in top_3:
 
            if elf_sum > elf:
                top_3.append(elf_sum)
                top_3.sort()
                if (len(top_3) == 4):
                    top_3.pop(0)
                break

        elf_sum = 0
    else:
        elf_sum += int(el)

for i in top_3:
    top_3_sum += int(i)



print(top_3)
print("top_3 sum:", top_3_sum)
print("Highest Calorie count: ", top_3[2])
