#!/bin/sh

LOGFILE="./install.log"
PATHREPO="https://github.com/jaraco/path.git"
TARGETDIR="./local_lib"
rm -f $LOGFILE

pip3 -V

if [ "`pip3 freeze --path $TARGETDIR`" != "" ]; then
	echo "path.py already installed to $TARGETDIR"
	echo "crushing it!"
	rm -rf "$TARGETDIR"
	exit 0
fi

echo "Installing path from $PATHREPO to $TARGETDIR"
pip3 install \
	--pre git+"$PATHREPO" \
	--target "$TARGETDIR" \
	--log "$LOGFILE"

echo "Test path.py:"

export PYTHONPATH="$TARGETDIR"
python3 my_program.py
