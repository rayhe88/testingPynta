#!/bin/bash

echo "Clean the filesystem for a pynta run"

echo "Clean the launch subdir"
rm -rf launcher_2023*

echo "Move to reaction dir"
cd reaction/

echo "Clean TS dir"
rm -rf TS*

echo "Move to Adsorbates dir"
cd Adsorbates/

echo "Move to CO[Pt] dir"
cd 'CO[Pt]'

echo "Remove files"
cd 0
rm -rf *.traj vib* weak* ?.xyz
cd ..

cd 1
rm -rf *.traj vib* weak* ?.xyz
cd ..

cd 2
rm -rf *.traj vib* weak* ?.xyz
cd ..

cd 3
rm -rf *.traj vib* weak* ?.xyz
cd ../..

echo "Move to OC[Pt] dir"
cd 'OC[Pt]'

echo "Remove files"
cd 0
rm -rf *.traj vib* weak* ?.xyz
cd ..

cd 1
rm -rf *.traj vib* weak* ?.xyz
cd ..

cd 2
rm -rf *.traj vib* weak* ?.xyz
cd ..

cd 3
rm -rf *.traj vib* weak* ?.xyz
