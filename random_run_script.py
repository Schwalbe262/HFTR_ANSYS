import yaml
import os
import subprocess
import random


REFERENCE_SCRIPT_FILE_NAME = "run_ansys_ref.py"

for i in range(1, 10): 
    
    run_simul(i)
    


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
    os.mkdir(folder_name)

    #2 Make Variable info file
    with open(os.path.join(folder_name,"info.yaml"), "w") as info_file:
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
    filepath = os.path.join(folder_name,f'run_ansys_{version_idx_str}.py')
    with open(filepath,"w") as f :
        f.write(ref_script_str)


    #4 run script in system.
    subprocess.run(["C:blablabla--FIXME--", "-runscript",filepath])



