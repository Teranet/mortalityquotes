#!/bin/bash 
FILE=/tmp/quote
QT=/tmp/die
if [ ! -f $FILE ]; then
	python quote.py > $FILE
fi

while [ : ]
do
	quote=$(sort --random-sort $FILE | head -n 1)

	 echo $quote|tr -cd '[:alnum:]\n\r '\''.' > $QT
	 wall -n $QT
	sleep 100
done



