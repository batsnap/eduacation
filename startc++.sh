#!/bin/bash

echo $0
echo $1
text=$1
g++ -lm -o ${text/.cpp/''} ${text/.cpp/''}.cpp; ./${text/.cpp/''};rm ${text/.cpp/''}
