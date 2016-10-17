while [ $# -gt 0 ]; do ## or: while [ -n "$*" ]; do
    echo $1
    shift
done
