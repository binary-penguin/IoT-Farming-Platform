#!/bin/bash

read v1
read v2

if (($v1 > $v2));
then
echo $v1;
else
echo $v2;
fi
