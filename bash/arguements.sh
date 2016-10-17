#!/bin/bash

# Using the arguements from the command line

filename="$0"
if [ $# != 1 ]
then
    echo 'number of arguements is not 1,\n Sorry!'
    exit 1
else
    echo "Your name is $1, first time in my life I've seen such a kolomeri" 
    exit 0
fi
