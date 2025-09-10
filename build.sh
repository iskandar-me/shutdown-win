#!/bin/bash

# delete old builds
rm -rf build dist shut.spec

# rebuild exe
python -m PyInstaller --onefile --noconsole --clean shut.py

# copy new exe to desktop
cp dist/shut.exe ~/Desktop/shut.exe

echo "✅ New shut.exe is ready on Desktop"
#!/bin/bash

# delete old builds
rm -rf build dist shut.spec

# rebuild exe silently
python -m PyInstaller --onefile --noconsole --clean shut.py

echo "✅ New shut.exe is ready in dist/"


