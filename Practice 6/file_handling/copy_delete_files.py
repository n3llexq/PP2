import os

if os.path.exists("sample_files/myfile.txt"):
  os.remove("sample_files/myfile.txt")
  print("File deleted")
else:
  print("The file does not exist")

source = "sample_files/myfile.txt"
destination = "sample_files/myfile_copy.txt"

if os.path.exists(source):
    try:
        with open(source, 'rb') as src_file:
            with open(destination, 'wb') as dest_file:
                dest_file.write(src_file.read())
        print("File copied successfully")
    except Exception as e:
        print(f"Error copying file: {e}")
else:
    print("The source file does not exist")