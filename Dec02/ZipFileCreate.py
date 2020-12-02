from zipfile import *
f = ZipFile("file.zip", 'w', ZIP_DEFLATED)
f.write("river.jpg")
f.write("fall.jpg")
f.close()
print("files.zip file created successfully")