import PyPDF2 
from os import listdir
from os.path import isfile, join

# get pdf filenames
dest_dir = 'extracted/'
src_dir = 'pdfs/'
src_files = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]

# get txt filesnames
dest_files = [f for f in listdir(dest_dir) if isfile(join(dest_dir, f))]

def alreadyExtracted(pdf_file, extracted_files):
    file = pdf_file.replace('pdf', 'txt')
    if (file in extracted_files):
        return True
    return False

# extract text for each pdf found
for pdf_file in src_files:
    # skip file if txt file found
    if (alreadyExtracted(pdf_file, dest_files)):
        # print(pdf_file + " already extracted! skipping...")
        continue

    src_path = src_dir + pdf_file

    # open pdf file for reading.
    pdfFileObj = open (src_path, 'rb')

    # create pdf reader object and read data
    reader = PyPDF2.PdfReader(pdfFileObj)
    pageObj = reader.pages[0]

    # create text file to store extracted data
    dest_path = dest_dir + pdf_file 
    dest_path = dest_path.replace('pdf', 'txt')
    fh = open(dest_path, 'w')
    
    # extract and write data
    try:
        fh.write(pageObj.extract_text())
    except:
        print("Error extracting from: " + src_path)
        continue

    # clean up.
    fh.close()
    pdfFileObj.close()