#!/bin/bash


# ij ~/workspace/GAStats/timeline.sql; gnuplot ~/workspace/GAStats/timeline.gp; pdf270 timeline.pdf;  pdfcrop timeline-rotated270.pdf; ~/workspace/GAStats/timespan.py 


awk -F "," '{ print $2-$1 }' timeline.dat | xargs echo > timeline-fix.dat
awk -F "," '{ print $3 }' timeline.dat | xargs echo >> timeline-fix.dat
awk -F "," '{ print $4 }' timeline.dat | xargs echo >> timeline-fix.dat
awk -F "," '{ print $5 }' timeline.dat | xargs echo >> timeline-fix.dat
