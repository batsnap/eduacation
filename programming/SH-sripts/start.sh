#!/bin/bash

echo $0
echo $1
text=$1
fpc ${text/.pas/''}.pas; ./${text/.pas/''}; rm ${text/.pas/''}; rm ${text/.pas/''}.o
