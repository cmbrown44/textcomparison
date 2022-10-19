# Import Module
import os
file_paths = [ ]
data = [ ]
#Folder Path
path = r"C:\Users\brown\PycharmProjects\OfficeHoursTextComparison\samples"
#Change the directory
os.chdir(path)
# Read text File

def read_text_file():
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{path}\{file}"
            file_paths.append(file_path)

    for file_path in file_paths:
        with open(file_path, 'r') as f:
            for line in f:
                #print(f.read())
                if not line.isspace():
                # print(line)
                    data.append({
                    line[0]: line[2:-1]
                    })
                print(data)


# iterate through all file


		# call read text file function
		#read_text_file(file_path)
print(file_paths)

read_text_file()




for file_path in file_paths:
    with open(path) as f:
        for line in f:
            if not line.isspace():
                #print(line)
                data.append({
                    line[0] : line[2:-1]
                })
print(data)