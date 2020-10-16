#!/bin/bash

if [[-d $1]];
then
echo It is a dir;
elif [[-f $1]];
then
echo It is a file;
else
echo NOOOOOO;
fi

