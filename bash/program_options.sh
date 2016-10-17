#!/usr/bin/env bash

progname=${0##*/}
verbose=0
filename=

# List the available command line options
# those options taht take arguments are followed by a colon
optstring=f:v

while getopts $optstring opt; do
    case $opt in
        f) filename=$OPTARG ;;
        v) verbose=$(( $verbose+1 )) ;;
        *) exit 1;;
    esac
done

# Remove options from the command line ## $OPTIND points to the next, unparsed
# argument
shift "$(( $OPTIND - 1 ))"

## Check whether a filename was entered
if [ -n "$filename" ]; then
    if [ $verbose -gt 0 ]; then
        printf "Filename is %s\n" "$filename"
    fi
else
    if [ $verbose -gt 0 ]; then
        printf "No filename entered\n" >&2
    fi
    exit 1
fi
## Check whether file exists
if [ -f "$filename" ]; then
    if [ $verbose -gt 0 ]; then
        printf "Filename %s found\n" "$filename"
fi

else
    if [ $verbose -gt 0 ]; then
        printf "File, %s, does not exist\n" "$filename" >&2
    fi
    exit 2
fi ## If the verbose option is selected,

## print the number of arguments remaining on the command line
if [ $verbose -gt 0 ]; then
    printf "Number of arguments is %d\n" "$#"
fi
