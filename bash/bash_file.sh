#!/bin/bash

cd ~
if [ -d kalimera.txt ]
then
    echo 'kalimera'
else
    echo 'there is no such file'
fi
