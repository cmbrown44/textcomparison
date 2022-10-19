# Open File in Read Mode
file_1 = open(r"C:\Users\brown\PycharmProjects\OfficeHoursTextComparison\text1.txt")
file_2 = open(r"C:\Users\brown\PycharmProjects\OfficeHoursTextComparison\text2.txt")

#print("Comparing files ", " @ " + 'file1.txt', " # " + 'file2.txt', sep='\n')

file_1_line = file_1.readline()
file_2_line = file_2.readline()

# Use as a COunter
line_no = 1

print()

with open(r"C:\Users\brown\PycharmProjects\OfficeHoursTextComparison\text1.txt") as file1:
    with open(r"C:\Users\brown\PycharmProjects\OfficeHoursTextComparison\text2.txt") as file2:
        same = set(file1).intersection(file2)

print("Common Lines in Both Files")

for line in same:
    print(line, end='')