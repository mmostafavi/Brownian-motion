![Brownian motion](Python-Project.gif)

## Contents
* atomic-number.pdf: step by step description to complete the project.
* run_1.zip to run10.zip: dataset to use in the project.
* mp4: a folder containing different movies displaying brownian motion of beads in water.
* beads-run_1.txt and displacements-run_1.txt: sample outputs for this project.

## Description
* this project is about proccesing consecutive frames of bead molecules among 
* water molecules and recognize beads from water and find their movement in small
* gaps of time in consecutive frames and use scientific formulas to estimate 
* avagrado Number with a good accuracy.

## Commands
* use <code>python beadtracker.py 25 180.0 25.0 run_1/*.jpg | python avagrado.py</code> for final result.
* in command above first argument is name of our file. second one (25) is min pixels that considered as bead.
* third command is brightness that a pixel has to be considered as bead pixel.
* fourth is maximum distance that we accept as movement in two consecutive frame for a bead molecule.
* fifth is the folder we want to use for calculation.
* feel free to change all them except first one.

* if you want to see just movements use command <code>python beadtracker.py 25 180.0 25.0 run_1/*.jpg </code>



* and ofcourse feel free to fork and maybe do it yourself 😉
