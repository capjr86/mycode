#!/usr/bin/env python3
#import shutil and os
import shutil
import os
#force program to start in home user directory
os.chdir("/home/student/mycode/")
#copy file from source and paste in destination
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#copy directory from source and paste in destination
shutil.copytree("5g_research/", "5g_research_backup/")

