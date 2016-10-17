#!/bin/bash

temp=$(mktemp /tmp/tempfile.XXXX)
echo $temp | tee $temp
