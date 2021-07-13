import yaml
import os
import subprocess
import random
import csv
import time
import csv
import numpy as np
import math



REFERENCE_SCRIPT_FILE_NAME = f'D:\\script\\run_ansys_ref_v2.py'
    

def run_simul(version_idx_str):
    #0 Initialize random variables
    d1 = 6.54
    move_tx = d1 + 3
    N1 = random.randrange(1,10)
    N2 = random.randrange(1,10)
    N = max(N1,N2)
    l1 = random.randrange(5,50)
    space2 = random.randrange(20,60)
    space1 = random.randrange(5,math.ceil(space2-d1-2))
    l2 = random.randrange(space2+20,100)
    h1 = random.randrange(math.ceil((N-1)*move_tx+2*d1),200)
    w1 =  random.randrange(30,200)
    air = max(2*l1+h1,4*l1+l2,w1+40+2*d1) + 50

    str_tx = f'Tx_in,Tx_out,Tx1,'
    Tx_loop = ""
    for i in range(1,N1) :

        str_tx = str_tx + f'Tx{i+1},'

        Tx_loop = Tx_loop + "oEditor.Paste()\n"
        Tx_loop = Tx_loop + "oEditor.Move(\n"
        Tx_loop = Tx_loop + "   [\n"
        Tx_loop = Tx_loop + f'    "NAME:Selections",\n'
        Tx_loop = Tx_loop + f'    "Selections:="		, "Tx{i+1}",\n'
        Tx_loop = Tx_loop + f'    "NewPartsModelFlag:="	, "Model"\n'
        Tx_loop = Tx_loop + "   ],\n"
        Tx_loop = Tx_loop + "   [\n"
        Tx_loop = Tx_loop + f'    "NAME:TranslateParameters",\n'
        Tx_loop = Tx_loop + f'    "TranslateVectorX:="	, "0",\n'
        Tx_loop = Tx_loop + f'    "TranslateVectorY:="	, "0",\n'
        Tx_loop = Tx_loop + f'    "TranslateVectorZ:="	, "-{i}*move_tx+offset_tx"\n'
        Tx_loop = Tx_loop + "   ])\n"
    str_tx = str_tx[:-1]

    str_rx = f'Rx_in,Rx_out,Rx1,'
    Rx_loop = ""
    for i in range(1,N2) :

        str_rx = str_rx + f'Rx{i+1},'

        Rx_loop = Rx_loop + "oEditor.Paste()\n"
        Rx_loop = Rx_loop + "oEditor.Move(\n"
        Rx_loop = Rx_loop + "   [\n"
        Rx_loop = Rx_loop + f'    "NAME:Selections",\n'
        Rx_loop = Rx_loop + f'    "Selections:="		, "Rx{i+1}",\n'
        Rx_loop = Rx_loop + f'    "NewPartsModelFlag:="	, "Model"\n'
        Rx_loop = Rx_loop + "   ],\n"
        Rx_loop = Rx_loop + "   [\n"
        Rx_loop = Rx_loop + f'    "NAME:TranslateParameters",\n'
        Rx_loop = Rx_loop + f'    "TranslateVectorX:="	, "0",\n'
        Rx_loop = Rx_loop + f'    "TranslateVectorY:="	, "0",\n'
        Rx_loop = Rx_loop + f'    "TranslateVectorZ:="	, "-{i}*move_rx+offset_rx"\n'
        Rx_loop = Rx_loop + "   ])\n"
    str_rx = str_rx[:-1]


    #FIXME : add some variables

    #0.5 Config Identifier-Variable set.
    config = {
        "$VERSION_IDX_STR"  :   version_idx_str,
        "$N1"              :   N1,
        "$N2"              :   N2,
        "$l1"              :   l1,
        "$l2"              :   l2,
        "$h1"              :   h1,
        "$w1"              :   w1,
        "$N1"              :   N1,
        "$N2"              :   N2,
        "$Tx_loop"              :   Tx_loop,
        "$str_tx"              :   str_tx,
        "$Rx_loop"              :   Rx_loop,
        "$str_rx"              :   str_rx,
        "$air"              :   air,
        "$space1"              :   space1,
        "$space2"              :   space2
        #FIXME : add some idt : variables
    }

    #1 Make Folder
    folder_name = f'SIMUL_{version_idx_str}'
    os.mkdir(f'D:\script\ML_v2\SIMUL_{version_idx_str}')

    #2 Make Variable info file
    with open(f'D:\script\ML_v2\SIMUL_{version_idx_str}\info.yaml', "w") as info_file:
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
    with open(f'D:\\script\\ML_v2\\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py',"w") as f :
        f.write(ref_script_str)


    #4 make batch file.
    
    filepath2 = os.path.join('ML_v2',folder_name,f'run_bat_{version_idx_str}.bat')
    with open(f'D:\\script\\ML_v2\\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat',"w") as f :
        f.write(f'"C:\\Program Files\\AnsysEM\\AnsysEM20.1\\Win64\\ansysedt.exe" -runscriptandexit "D:\\script\\ML_v2\\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py"')

    workingDir = f'D:\script\ML_v2\SIMUL_{version_idx_str}'
    executeFile = f'D:\script\ML_v2\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat'
    os.chdir(workingDir)
    os.system(executeFile)
    
    with open(f'D:\script\ML_v2_data\Data {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)

        for line in rdr:
            a = 1
            
    with open(f'D:\script\ML_v2_data\Data.csv',"a", encoding='utf-8', newline='') as f :
        
        tmp = np.concatenate((N1, N2, space1, space2, l1, l2, h1, w1, line[1], line[2], line[3], line[4], line[5]), axis=None)
        wr = csv.writer(f)
        wr.writerow(tmp)
            

    


for i in range(1, 1001): 

    try :
        run_simul(i)
        os.remove(f'D:\script\ML_aedt\ML_v2.aedt.lock')
    except :
        time.sleep(1)	

    
    time.sleep(1)
