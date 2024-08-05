# This script writes filenames from directory to terminal.

from os import listdir
from os.path import isfile, join

# place extracted file names in a list.
dest_dir = 'output/extracted_pdfs/'
dest_files = [f for f in listdir(dest_dir) if isfile(join(dest_dir, f))]

def writeFilenames():
    """Helper function for outputting filenames in a directory."""
    for fn in dest_files:
        print(fn)

writeFilenames()