#!/bin/bash

# Functions Used
add () {
    #out=$(($1 + $2))
    out=$(echo $1 + $2 | bc)
    echo "The out of the numbers $1 $2 is: $out"
}
substract () {
    out=$(echo $1 - $2 | bc)
    echo "The out of the numbers $1 $2 is: $out"
}
multiply () {
    #out=$(echo $1 * $2 | bc)
    out=$(echo $1 \* $2 | bc)
    echo "The out of the numbers $1 $2 is: $out"
}
divide () {
    out=$(echo $1 / $2 | bc)
    echo "The out of the numbers $1 $2 is: $out"
}


# Declaring the Data
num1=$1 ; num2=$2 ; operator=$3
echo "The first number given is $num1"
echo "The second number given is $num2"
echo "The operator is $operator"

# Conditional for function choice

if [ "$operator" == "p" ] ; then
    add $num1 $num2
elif [ "$operator" == "m" ] ; then
    substract $num1 $num2
elif [ "$operator" == "t" ] ; then
    multiply $num1 $num2
elif [ "$operator" == "o" ] ; then
    divide $num1 $num2
else 
    echo "Pick a valid operator"
fi

