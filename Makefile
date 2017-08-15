all:
	cd src;	qmake;	make
	cd sip; python configure.py; make
