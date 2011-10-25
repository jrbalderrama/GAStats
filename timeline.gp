### gnuplot ~/workspace/GAStats/timeline.gp; pdf270 timeline.pdf;  pdfcrop timeline-rotated270.pdf

reset 

set style line 80 linetype 1 linecolor rgb "#808080" linewidth 2
set style line 81 lt 0 lc rgb "#808080"

set style line 1 lt rgb "#A00000" lw 2 pt 1 ### red
set style line 2 lt rgb "#00A000" lw 2 pt 6 ### green 
set style line 3 lt rgb "#5060D0" lw 2 pt 2 ### blue 
set style line 4 lt rgb "#F25900" lw 2 pt 9 ### orange

set style line 11 lc rgb "#AF2626" ### brick ---PANTONE 1805
set style line 22 lc rgb "#AFAF26" ### olive ---complementary of river
set style line 33 lc rgb "#26AF26" ### grass ---triadic of brick
set style line 44 lc rgb "#2626AF" ### river ---triadic of brick

set style data histogram
set style histogram columnstacked
set style fill solid noborder 

set key off
set size ratio 2
set boxwidth 1 absolute
set datafile separator ","
set border front 9 # linestyle 80
set grid front noxtics y2tics linestyle 81


unset ytics 
set xtics in rotate by 90 mirror 
set y2tics out rotate by 90 nomirror
set xrange [ 0 : * ] reverse 
set yrange [ 0 : * ] noreverse nowriteback

set y2label "Time [s]" offset -1.5
# set label 1 "Jobs" at graph 0.5, -0.1 centre rotate by 180

set terminal png transparent crop enhanced font "/home/javier/.fonts/Ronnia-regular.ttf" 25 size 1680,1280
set output 'timeline.png'

# plot "timeline.dat" using ($1 + $2 + $3 + $4 + $5) with boxes linestyle 44 title "UPLOAD", \
#      "" u ($1 + $2 + $3 + $4) w boxes ls 33 t "RUNNING", \
#      "" u ($1 + $2 + $3) w boxes ls 22 t "DOWNLOAD",\
#      "" u ($1 + $2) w boxes ls 11 t "QUEUED", \
#      "" u 1 w boxes lt -2 notitle 


# plot "timeline.dat" using ($1 + $2 + $3 + $4 + $5) with boxes linetype 3 title "UPLOAD", \
#      "" u ($1 + $2 + $3 + $4) w boxes lt 2 t "RUNNING", \
#      "" u ($1 + $2 + $3) w boxes lt 6 t "DOWNLOAD",\
#      "" u ($1 + $2) w boxes lt 1 t "QUEUED", \
#      "" u 1 w boxes lt -2 notitle 


plot "timeline.dat" using ($2 + $3 + $4 + $5) with boxes linestyle 44 title "UPLOAD", \
     "" u ($2 + $3 + $4) w boxes ls 33 t "RUNNING", \
     "" u ($2 + $3) w boxes ls 22 t "DOWNLOAD",\
     "" u 2 w boxes ls 11 t "QUEUED", \
     "" u 1 w boxes lt -2 notitle 

set terminal postscript portrait enhanced color fontfile "/home/javier/.fonts/Ronnia-regular.ttf" font "Ronnia-Regular,20"
set output 'timeline.ps'
#set output '| ps2pdf - timeline.pdf'

#set terminal pdfcairo font "Gill Sans,9" linewidth 4 rounded
#set output 'timeline.pdf'

replot
