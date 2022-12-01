with open("./1/input.txt", "r") as f:
    data = f.read()

split = data.split("\n\n")

elf_calories_list = [
    sum([int(item) for item in elf_str_list.split("\n")])
    for elf_str_list in data.split("\n\n")
]

sorted_calories = sorted(elf_calories_list, reverse=True)

max_calories = sorted_calories[0]
top_three = sum(sorted_calories[:3])

print(max_calories)
print(top_three)

