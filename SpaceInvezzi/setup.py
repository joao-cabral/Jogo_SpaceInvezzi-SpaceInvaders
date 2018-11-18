import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("Trabalho.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)




setup(
    name = "Star-Wars",
    version = "1.0",
    description = "Jogo feito por Matheus Barros e João Cabral",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
