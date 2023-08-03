import sys
#sys.path.append("/home/rayhe/Github/pynta")
sys.path.append("/home/rayhe/Github/pyntaOrigin/pynta")

import os
import shutil
from pynta.main import *
from pynta.utils import clean_pynta_path
from fireworks import LaunchPad, Workflow
from fireworks.core.rocket_launcher import rapidfire, launch_rocket
from fireworks.features.multi_launcher import launch_multiprocess
from fireworks.flask_site.app import app

def mypause(flag):
    print("\033[32;49;1m {0:20s}\033[0m ".format(flag))
    # green 32
    # blue  34
    # red   31

def run():

    path='/home/rayhe/Work/pyntaTest7/reaction'
    name='Test_R2D22'
    lpad = LaunchPad()
    lpad.reset('', require_password=False)

    command = '/home/rayhe/Downloads/qe-7.1/bin/pw.x < PREFIX.pwi > PREFIX.pwo'

    pseudo = {'C': 'C.pbe-n-kjpaw_psl.1.0.0.UPF',
            'O': 'O.pbe-n-kjpaw_psl.1.0.0.UPF',
            'Cu': 'Cu.pbe-spn-kjpaw_psl.1.0.0.UPF',
            'H': 'H.pbe-kjpaw_psl.1.0.0.UPF'}

    conf_qe = { 'kpts':(4,4,1), 'ecutwfc': 40, 'tprnfor': True,
                'pseudo_dir' : '/home/rayhe/espresso/pseudo',
                'occupations':'smearing', 'smearing':'gauss', 'input_dft':'PBE',
                'degauss':0.01, 'nosym':True, 'mixing_mode':'local-TF',
                'pseudopotentials':pseudo, 'conv_thr': 1e-6, 'command':command}


    pyn = Pynta(path=path,
            rxns_file=os.path.join(path,"rxn_test.yaml"),
            software="XTB",
            surface_type="fcc111",metal="Cu",socket=False,queue=False,a=3.61,
            repeats=(3,3,4),
            label=name,num_jobs=8,max_num_hfsp_opts=4,
            #software_kwargs     = conf_qe,
            #software_kwargs_gas = conf_qe,
            software_kwargs    ={"method": "GFN1-xTB", "fake" : "origin0"},
            software_kwargs_gas={"method": "GFN1-xTB", "fake" : "origin1"},
            TS_opt_software_kwargs={"fake": "origin2"},
            lattice_opt_software_kwargs={"fake": "origin3"},
           slab_path=os.path.join(path,"slab.xyz"),frozen_layers=4 #new
           )

    mypause("excute_from_initial_ad_guesses")
    pyn.execute_from_initial_ad_guesses()

    mypause("End of test_workflow")

if __name__ == '__main__':

    mypause("Before unittest main")
    run()
    mypause("After unittest main")
