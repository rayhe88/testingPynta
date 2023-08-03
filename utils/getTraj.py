import os
import fnmatch
import shutil

from ase.io.trajectory import Trajectory
from ase.io import read, write

def remove_path_before_string(path, target_string):
    index = path.find(target_string)
    if index != -1:
        return path[index:]
    else:
        return path

def getNumSimulations(path, num, dest_path):
    #traj = Trajectory(path)
    atoms = read(path, index=':')

    print("{0:45s}".format(remove_path_before_string(path, 'reaction')), end='')

    newfile = "{0}/file{1:02d}.extxyz".format(dest_path, num)

    write(newfile,atoms, format='extxyz')

    print("idx: {0:02d}".format(num), end='')

    avat = 0
    for at in atoms:
        avat += len(at)

    avat /= len(atoms)

    print(" ava: {0:7.3f} ".format(avat), end='')
    print(" There are {0:6d} simulations".format(num))

    return len(atoms)


def run(root, trajsub, ext):
    numTotal = 0
    nfile = 0
    for path, dirs, files in os.walk(root):
        for filename in fnmatch.filter(files, ext):
            file_path = os.path.join(path, filename)
            num = getNumSimulations(file_path, nfile, trajsub)
            numTotal += num
            nfile += 1
    return numTotal

if __name__ == '__main__':

    root_path = '/home/rayhe/Work/pyntaTest7/reaction'
    traj_path = '/home/rayhe/Work/pyntaTest7/trajFiles'

    tot = run(root_path,traj_path,'*.traj')

    print(" Total simulations in this reaction: ",tot)
