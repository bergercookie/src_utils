#!/usr/bin/env bash

function my_fun {
    echo "${@: -1}"
    echo $a
}

export a=1
my_fun first second third
