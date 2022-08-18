import os
import shutil
from Files import Files

class Folder(Files):
    def __init__(self, path):
        super().__init__(path)
    # Deleting a directory
    def deleteDir(self):
        
        if os.path.isdir(self.path):  
            shutil.rmtree(self.path)
        else:
            message ="Directory does not exist"    
            
    # Copying directory
    def copyDir(src, dst):
    
        if os.path.isdir(src):
            shutil.copytree(src, dst+src[1:])
            message ="Directory has been copied"
        else:
            message ="Directory does not exist"