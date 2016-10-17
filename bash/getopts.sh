progname=${0##*/}
num_args=$#
arg1=$1
arg2=$2
last_arg=${@:$#} 
all_args=$@

printf "progname: %s\n" "$progname"
printf "number of arguments: %s\n" "$num_args"
printf "argument 1: %s\n" "$arg1"
printf "argument 2: %s\n" "$arg2"
printf "last argument: %s\n" "$last_arg"
printf "all argument: %s\n" "$all_args"

optstring=a:b:cd

while getopts $optstring opt; do
    case $opt in
        a) echo "a - arg = ${OPTARG}" ;;
        b) echo "b - arg = ${OPTARG}" ;;
        c) echo "c was entered." ;;
        d) echo "d was entered." ;;
    esac
done
