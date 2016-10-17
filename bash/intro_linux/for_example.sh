#!/bin/bash

sum=0
for i in 1 2 3 4 5 6 7 8 9 984
do
    sum=$(( $sum + $i ))
    echo "Current Sum is $sum"
    sleep 1
done

echo "the sum is $sum"
