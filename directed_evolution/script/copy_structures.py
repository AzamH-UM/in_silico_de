import os
from pathlib import Path
from zipfile import ZipFile
import shutil

SCREEN_DIR = Path("/home/azamh/anc_iter/evolib/screen")
STRUCTURE_DIR = SCREEN_DIR / "structures"
LIBRARY_RESULTS_DIR = SCREEN_DIR / "library_data"
RESULTS_COPY_DIR = Path('/home/azamh/isde_article/directed_evolution/computational_results')

SUB_LIBRARIES = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
LIBRARIES = ['wt', "r1", "r2", "r3", "r4"] + \
    [f'r0{x}' for x in SUB_LIBRARIES] + \
    [f'r1{x}' for x in SUB_LIBRARIES] + \
    [f'r2{x}' for x in SUB_LIBRARIES] + \
    [f'r3{x}' for x in SUB_LIBRARIES]
print(LIBRARIES)

for library in LIBRARIES:
    library_results_xlsx = LIBRARY_RESULTS_DIR / f"{library}_screen.xlsx"
    assert library_results_xlsx.exists()
    # shutil.copyfile(library_results_xlsx, RESULTS_COPY_DIR / f"{library}.xlsx")

    