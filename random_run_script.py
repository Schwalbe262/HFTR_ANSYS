import yaml
import os
import subprocess
import random
import csv
import time
import csv
import numpy as np



REFERENCE_SCRIPT_FILE_NAME = f'D:\\script\\run_ansys_ref.py'
#REFERENCE_SCRIPT_FILE_NAME = "run_ansys_ref.py"
    

def run_simul(version_idx_str):
    #0 Initialize random variables
    l1 = random.randrange(10,50) #FIXME : change random range.
    l2 = random.randrange(50,100)
    h1 = random.randrange(50,150)
    w1 =  random.randrange(30,200)
    #FIXME : add some variables

    #0.5 Config Identifier-Variable set.
    config = {
        "$VERSION_IDX_STR"  :   version_idx_str,
        "$l1"              :   l1,
        "$l2"              :   l2,
        "$h1"              :   h1,
        "$w1"              :   w1
        #FIXME : add some idt : variables
    }

    #1 Make Folder
    folder_name = f'SIMUL_{version_idx_str}'
    #os.mkdir(folder_name)
    #os.mkdir(os.path.join('ML_v1',folder_name))
    os.mkdir(f'D:\script\ML_v1\SIMUL_{version_idx_str}')

    #2 Make Variable info file
    #with open(os.path.join(folder_name,"info.yaml"), "w") as info_file:
    #with open(os.path.join('ML_v1',folder_name,"info.yaml"), "w") as info_file:
    with open(f'D:\script\ML_v1\SIMUL_{version_idx_str}\info.yaml', "w") as info_file:
        yaml.dump(config,info_file)

    #3 Make python script file
    #Load file string
    ref_script_str = ""
    with open(REFERENCE_SCRIPT_FILE_NAME) as f :
        lines = f.readlines()
    ref_script_str = "\n".join(lines);

    #Change Identifiers
    for idt, var in config.items() :
        ref_script_str = ref_script_str.replace(idt, str(var))

    #Save file
    #filepath = 'D:\script\ML_v1\run_ansys_{version_idx_str}.py'
    filepath = os.path.join('ML_v1',folder_name,f'run_ansys_{version_idx_str}.py')
    with open(f'D:\\script\\ML_v1\\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py',"w") as f :
        f.write(ref_script_str)


    #4 run script in system.
    #subprocess.run(["C:\Program Files\AnsysEM\AnsysEM20.1\Win64\ansysedt.exe ", "-runscriptandexit D:\script\\", filepath])
    
    #4 make batch file.
    
    filepath2 = os.path.join('ML_v1',folder_name,f'run_bat_{version_idx_str}.bat')
    with open(f'D:\\script\\ML_v1\\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat',"w") as f :
        f.write(f'"C:\\Program Files\\AnsysEM\\AnsysEM20.1\\Win64\\ansysedt.exe" -runscriptandexit "D:\\script\\ML_v1\\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py"')
        
    workingDir = f'D:\script\ML_v1\SIMUL_{version_idx_str}'
    executeFile = f'D:\script\ML_v1\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat'
    os.chdir(workingDir)
    os.system(executeFile)
    
    with open(f'D:\script\ML_v1_data\Data {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)

        for line in rdr:
            a = 1
            
    with open(f'D:\script\ML_v1_data\Data.csv',"a", encoding='utf-8', newline='') as f :
        
        tmp = np.concatenate((l1, l2, h1, w1, line[1], line[2], line[3], line[4], line[5]), axis=None)
        wr = csv.writer(f)
        wr.writerow(tmp)
            

    


for i in range(195, 1001): 

    try :
        run_simul(i)
    except :
        time.sleep(1)	

    
    time.sleep(1)
