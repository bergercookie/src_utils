# variable a is unset
echo ${var:-default_value} # -> default_value

var=
echo ${var:-default_value} # -> default_value

var=a
echo ${var:-default_value} # -> $var


