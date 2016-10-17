echo "Input a name..."
read name

if [ -n "$name" ]; then
    printf "Entered name is: %s\n" "$name"
else
    echo "Name is empty..."
fi

echo "Testing first two letters..."
if [[ ${name:0:1} == "k" ]] && [[ ${name:1:1} == "a" ]]; then
    echo "first two letters are ka"
else
    echo "first two letters are NOT ka"
fi
