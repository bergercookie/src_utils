#!/bin/bash

# Constant Initialization
dump_dev=/dev/null

echo "Give me a directory name to ls on it"
read file_name


if [[ -e $file_name ]]
then
    ls -l $file_name > dump_dev
else
    echo "No such file!"
fi

echo "The return code is $?"

