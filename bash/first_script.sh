#!/opt/local/bin/bash

: '
MANIFESTO
this is the start of the bash learnign process
read comments below
'


echo "hello $USER!. I wish to list some files of yours"
echo "listing files in the current directory, which is: $PWD"

ls # list the damn files

# Variable definition
x="hello mum"
y=hello # if it is a one-word variable the " aren't needed

# Variable reference
echo "this is my variable: $x"

: '
Use SINGLE quotes if no variable names are included => more predictable! but
use DOUBLE quotes else
'
echo -n '$USER=' # -n option stops echo from breaking the line
echo "$USER"

# or you can escape the $ character
echo "\$USER=$USER 2nd version"

if [ -n "$X" ]; then # -n tests to see if the arguement is non empty, REMEMBER TO USE the DOUBLE quotes
    echo "the variable X is not the empty string"
fi

# shell expands variables
LS="ls"
LS_FLAGS="-al"

$LS $LS_FLAGS $PWD

# protecting variables -> { }
echo "${x}abc"
#echo "$xabc" # this is WRONG. Tries to find the var xabc

# conditionals
# operand1<space>operator<space>operand2
# Use quotes all the time

j=1
k=2

if [ "$j"="$2" ]; then
    echo "kalimera"
elif [ "$j" -gt "$k" ]; then
    echo "kalinuxta"
elif [ "$j" -lt "$k" ]; then
    echo "ok its the third already"
fi

# file type recognition

X=3
Y=4
empty_string=""
if [ $X -lt $Y ]; then	# is $X less than $Y ?
	echo "\$X=${X}, which is smaller than \$Y=${Y}"
fi

if [ -n "$empty_string" ]; then
	echo "empty string is non_empty"
fi

if [ -e "${HOME}/.fvwmrc" ]; then 			# test to see if ~/.fvwmrc exists
	echo "you have a .fvwmrc file"
	if [ -L "${HOME}/.fvwmrc" ]; then 		# is it a symlink ?  
		echo "it's a symbolic link"
	elif [ -f "${HOME}/.fvwmrc" ]; then 	# is it a regular file ?
		echo "it's a regular file"
	fi
else
	echo "you have no .fvwmrc file"
fi

if [[ -d "${HOME}/Desktop" ]]; then
    files_inside_home="ls -lrt ${HOME}"
    $files_inside_home
    file="${files_inside_home}/Downloads/clock-wide.jpg" 
    $file
     if [[ -n "${files_inside_home}/Downloads/clock-wide.jpg" ]]; then
         echo 'found it'
     fi
fi
for x in red green blue
do
    echo -n "$x "
done
echo

for (( makarios = 0; makarios < 100; makarios++ )); do
    echo kalimera
    echo kalinuxta
    echo 'vre den pas na gamithis'
    echo
done

# list all the files that start with D in ~
echo ${HOME}/D*


# I guess I learned some bash till now! ;)
