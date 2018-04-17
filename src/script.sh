mkdir -p ../installer/usr/share/meriones 2>/dev/null
cp  merionesmathlib.py ../installer/usr/share/meriones/merionesmathlib.py
cp  calculator.py ../installer/usr/share/meriones/calculator.py
cp  main.py ../installer/usr/share/meriones/main.py && chmod +x ../installer/usr/share/meriones/main.py
cp  icons8-hamster-50.png ../installer/usr/share/meriones/icons8-hamster-50.png
cp  ui_calculator_advanced.py ../installer/usr/share/meriones/ui_calculator_advanced.py
cp  ui_calculator.py ../installer/usr/share/meriones/ui_calculator.py
mkdir -p ../installer/usr/local/bin 2>/dev/null
ln -sf /usr/share/meriones/main.py ../installer/usr/local/bin/meriones-calculator
mkdir ../installer/tmp 2>/dev/null
cp requirements.txt ../installer/tmp/requirements.txt
chmod +x ../installer/DEBIAN/postinst
dpkg-deb --build ../installer/ ../installer/installer.deb
