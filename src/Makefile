#Meriones Makefile

.PHONY: all pip init pack packfolder clean test doc run installer

vpath %.py ../tests

#prelozi projekt vcetne programu pro profilling
all: pip run	
	
pip: 
	pip3 freeze
	
init:
	pip3 install -r requirements.txt
    
#zabali projekt tak aby mohl byt odevzdan
pack: doc packfolder meriones/xchlup08_xkinst01_xsaran02_xwysog00.zip
meriones/xchlup08_xkinst01_xsaran02_xwysog00.zip:
	rm -rf ../../xchlup08_xkinst01_xsaran02_xwysog00/repo/installer
	rm -rf ../../xchlup08_xkinst01_xsaran02_xwysog00/repo/doc	
	cd ../.. && zip -r $@ xchlup08_xkinst01_xsaran02_xwysog00
	
packfolder:
	mkdir -p ../../xchlup08_xkinst01_xsaran02_xwysog00/repo
	mkdir ../../xchlup08_xkinst01_xsaran02_xwysog00/installer
	mkdir ../../xchlup08_xkinst01_xsaran02_xwysog00/doc
	cp -a ../../meriones/. ../../xchlup08_xkinst01_xsaran02_xwysog00/repo/
	cp -a ../doc/. ../../xchlup08_xkinst01_xsaran02_xwysog00/doc/
	cp -a ../installer/. ../../xchlup08_xkinst01_xsaran02_xwysog00/installer/

#smazen vsechny soubory, co nemaji byt odevzdany
clean: 
	rm -rf ../installer/usr/ ../installer/DEBIAN/ ../../xchlup08_xkinst01_xsaran02_xwysog00

#spusti testy matematicke knihovny
test: merionesmathlib_tests.py
	cd .. && python3 -m src.merionesmathlib_tests

#spusti generovani dokumentace
doc: Doxyfile
	cd .. && mkdir doc && cd doc && doxygen ../src/$^

#spusti program
run: main.py
	python3 main.py 

installer: main.py merionesmathlib.py calculator.py ui_calculator_advanced.py ui_calculator.py requirements.txt
	bash script.sh
