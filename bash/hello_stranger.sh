printf "hello, %s!\n" "$1"

echo -e "\nListing some special parameters...\n"
printf "Number of arguments using #: %.2f\n" "$#"
echo "All the positional arguments using @: $@"
echo "All the positional arguments using *: $*"
echo "Path to script using 0: $0"

printf "%s " "All the positional arguments: $@"
echo
echo

echo -n No newline, BSD way
echo
echo -e "No newline, System V way\c"
