#Meriones Makefile

.PHONY: all pack clean test doc run

#prelozi projekt vcetne programu pro profilling
all: 
	pip3 freeze

init:
	pip3 install -r requirements.txt
    
#zabali projekt tak aby mohl byt odevzdan
pack: ../xchlup08_xkinst02_xsaran02_xwysog00.zip
../xchlup08_xkinst02_xsaran02_xwysog00.zip:
	mv ../../meriones ../../xchlup08_xkinst02_xsaran02_xwysog00
	zip -r $@ ../../xchlup08_xkinst02_xsaran02_xwysog00
	mv ../../xchlup08_xkinst02_xsaran02_xwysog00 ../../meriones	

#smazen vsechny soubory, co nemaji byt odevzdany ???
clean:

#spusti testy matematicke knihovny
test: ../tests/merioneslib_tests
	python3 -m $^

#spusti generovani dokumentace
doc: merionesmathlib.py
	cd .. && mkdir doc && cd doc && doxygen ../src/$^

#spusti program
run: main.py
	python3 main.py 
