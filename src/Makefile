#Meriones Makefile

.PHONY: all pip init pack clean test doc run installer

vpath %.py ../tests

#prelozi projekt vcetne programu pro profilling
all: pip run	
	
pip: 
	pip3 freeze
	
init:
	pip3 install -r requirements.txt
    
#zabali projekt tak aby mohl byt odevzdan
pack: doc ../xchlup08_xkinst01_xsaran02_xwysog00.zip
../xchlup08_xkinst01_xsaran02_xwysog00.zip:
	mv ../../meriones ../../xchlup08_xkinst01_xsaran02_xwysog00
	zip -r $@ ../../xchlup08_xkinst01_xsaran02_xwysog00
	mv ../../xchlup08_xkinst01_xsaran02_xwysog00 ../../meriones	

#smazen vsechny soubory, co nemaji byt odevzdany
clean: ../installer/usr ../installer/DEBIAN
	rm -rf $^

#spusti testy matematicke knihovny
test: merioneslib_tests.py
	cd .. && python3 -m $(patsubst ../tests/%.py,tests.%,$^)

#spusti generovani dokumentace
doc: Doxyfile
	cd .. && mkdir doc && cd doc && doxygen ../src/$^

#spusti program
run: main.py
	python3 main.py 

installer: main.py merionesmathlib.py calculator.py ui_calculator_advanced.py ui_calculator.py requirements.txt
	bash script.sh
