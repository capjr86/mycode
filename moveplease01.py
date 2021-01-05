#!/usr/bin/env python3
import shutil
import os
#execute file from specified directory
os.chdir('/home/student/mycode/')
#move file from source to new destination
shutil.move('raynor.obj', 'ceph_storage/')
#ask user for input
xname = input('What is the new name for kerrigan.obj? ')
#move and rename file based on user input
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

