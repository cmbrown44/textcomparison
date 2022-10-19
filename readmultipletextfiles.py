# Import Module
import os

#Folder Path
path = r"C:\Users\brown\PycharmProjects\OfficeHoursTextComparison"

#Change the directory
os.chdir(path)

# Read text File

file_paths = [ ]

def read_text_file(file_path):
	with open(file_path, 'r') as f:
		print(f.read())


# iterate through all file
for file in os.listdir():
	# Check whether file is in text format or not
	if file.endswith(".txt"):
		file_path = f"{path}\{file}"
		file_paths.append(file_path)

		# call read text file function
		read_text_file(file_path)
		print(file_paths)
