import zipfile as z

#set the target file
target = 'xxxx.zip' #enter the zip file name

#display a start message
print('Starting to Unzip the File!')

#use ZipFile method
root = z.ZipFile(target)

#give destination path
root.extractall('new')
root.close()

#display the end message
print('\nFile is Succesfully Unzipped!')