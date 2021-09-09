#!/bin/sh
curl $1 2> /dev/null | grep href | cut -d \" -f 2
