# force-web

The program currently only runs on mac and linux computers.  The executable is located in the dist/ folder. Put it in the same folder as the .csv file and then it will build the graph.

pyinstaller command to build to exe
pyinstaller -Fd main.py --hiddenimport=texttable --hiddenimport=cairo

