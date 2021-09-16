import sys
import cx_Freeze

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["pygame", "time", "sys", "os"],
                     "excludes": ["matplotlib.tests",
                                  "numpy.random._examples",
                                  "pandas",
                                  "scipy",
                                  "tensorflow"],
                     "include_files":["Resources", 'Scenes', 'Scripts', "options.ini"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

cx_Freeze.setup(  name = "Game",
        version = "0.1",
        description = "Game Description!",
        options = {"build_exe": build_exe_options},
        executables = [cx_Freeze.Executable("main.py", base=base)])

#run this on the command line interpreter
#python setup.py build_exe --excludes=matplotlib.tests,numpy.random._examples
