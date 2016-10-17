#!/usr/bin/env bash

if [[ "${x+X}" == X ]]; then # is $x set?
    if [ -n "$x" ]; then # if not empty
        printf "\$x = %s\n" "$x"
    else
        printf "\$x is set but empty \n"
    fi
else
    printf " %s is not set\n" "\$x"
fi

