#!/bin/bash

ORIGNAME=gnome-globalmenu
VERSION=0.9
GIT_REVISION=e4502d33b2
NAME=${ORIGNAME}-${VERSION}.git

rm -rf ${ORIGNAME}
git clone git://github.com/gnome-globalmenu/gnome-globalmenu.git &>/dev/null
cd $ORIGNAME
git checkout gnome-3
rm -rf .git
cd ..
mv ${ORIGNAME} ${NAME}

tar cfJ ${NAME}.tar.xz ${NAME}
rm -rf ${NAME}
