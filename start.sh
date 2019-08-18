#!/bin/bash

echo $0
echo $1
text=$1
mono /home/batyr/PABC/pabcnetc.exe ${text/.pas/''}.pas; mono ${text/.pas/''}.exe; rm ${text/.pas/''}.exe; rm ${text/.pas/''}.exe.mdb
