from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import sys
import os
import zipfile
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
def zipdir(dirPath, zipFilePath=None, includeDirInZip=True):
	if not zipFilePath:
		zipFilePath = dirPath + ".zip"
	if not os.path.isdir(dirPath):
		raise OSError("dirPath argument must point to a directory. "
					"'%s' does not." % dirPath)
	parentDir, dirToZip = os.path.split(dirPath)
	def trimPath(path):
		archivePath = path.replace(parentDir, "", 1)
		if parentDir:
			archivePath = archivePath.replace(os.path.sep, "", 1)
		if not includeDirInZip:
			archivePath = archivePath.replace(dirToZip + os.path.sep, "", 1)
		return os.path.normcase(archivePath)

	outFile = zipfile.ZipFile(zipFilePath, "w",
							compression=zipfile.ZIP_DEFLATED)
	for (archiveDirPath, dirNames, fileNames) in os.walk(dirPath):
		for fileName in fileNames:
			filePath = os.path.join(archiveDirPath, fileName)
			outFile.write(filePath, trimPath(filePath))
		if not fileNames and not dirNames:
			zipInfo = zipfile.ZipInfo(trimPath(archiveDirPath) + "/")
			outFile.writestr(zipInfo, "")
	outFile.close()
location= input("Enter the path of your file: ")
user_input=os.path.isdir(location)
user_input
if user_input is  True:
	print("path exists")	
	file1 =zipdir(location)
	print("File Converted into Zip")
	file1 = drive.CreateFile() 
	file1.SetContentFile(location +'.zip')
	file1.Upload()
else:
	print("invalid path")
print("file uploaded")
	
	
	
	