import glob
import os
home = os.getcwd()
directory_list = glob.glob("obq_weekend/obq*")
for item in directory_list:
    os.chdir(item)
    print("Entering: "+ item)
    os.system("vplanet vpl.in")
    os.chdir(home)
    