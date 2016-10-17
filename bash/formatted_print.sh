# Fri Aug 26 18:08:47 EEST 2016, Nikos Koukis
# Using printf to format random strings

min=1
max=100
for i in $(seq $min $max); do
    printf "%+5s.%-5s\n" $RANDOM $RANDOM
done
