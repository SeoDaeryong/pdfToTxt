#!/bin/sh -x

END_COUNT=$1
count=$2
lcount=`expr $count + 7`
while [ $count -le $END_COUNT ]
do
    date=`gdate -d "$count days ago" +%y%m%d`
    ldate=`gdate -d "$lcount days ago" +%y%m%d`
    #echo $date
    #echo $ldate
    if [ ! -s $date.pdf ]; then
        wget http://weekly.manmin.or.kr/pdf/$date.pdf
    fi
    if [ ! -s $ldate.pdf ]; then
        wget http://weekly.manmin.or.kr/pdf/$ldate.pdf
    fi
    python pdfToText.py $date.pdf
    python pdfToText.py $ldate.pdf
    python diff.py $ldate.txt $date.txt
    count=`expr $count + 7`
    lcount=`expr $lcount + 7`
done
