echo "Enter a number"; read number

case $number in
    1) echo "You entered the number 1";;
    2) echo "You entered the number 2";;
    *) echo "You entered something different than 1 or 2";;
esac
