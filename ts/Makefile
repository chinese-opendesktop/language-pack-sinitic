# lconvert --drop-translations foobar_*.qm -o foobar.ts

build:
	make -C Qt4 build
	make -C Qt5 build
	make -C miscdir build
	make -C translations build
	make -C LXQt build
	make -C sysdir build
	make -C leechcraft build
	make -C embed build

install:
	make -C Qt4 install
	make -C Qt5 install
	make -C miscdir install
	make -C translations install
	make -C LXQt install
	make -C sysdir install
	make -C leechcraft install
