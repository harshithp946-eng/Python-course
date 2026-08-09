import os

# Specify the directory path
path = "/"   # Current directory

# Get the list of files and folders
contents = os.listdir(path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)