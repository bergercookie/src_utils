# Input
printf "Give me a number..."
read number

# Input validation
case $number in
    *[!0-9]*) false ;;
*) echo "Invalid nmber: $number";;
esac

# User to enter  number > 20
lim=20
while [ ! $number -ge $lim ]; then
    printf "%d is not graeter or equal to %d" "$number" $lim"
    read number
done
