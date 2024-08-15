import PyPDF2 
from os import listdir
from os.path import isfile, join


def alreadyExtracted(pdf_file, extracted_files):
    file = pdf_file.replace('pdf', 'txt')
    if (file in extracted_files):
        return True
    return False


def main():
    # get pdf filenames
    src_dir = 'input/raw_pdfs/'
    src_files = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]

    # get txt filesnames
    dest_dir = 'output/extracted_pdfs/'
    dest_files = [f for f in listdir(dest_dir) if isfile(join(dest_dir, f))]

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

        # change file extension on destination file path from pdf to txt
        pdf_file = pdf_file.replace('pdf', 'txt')

        # create full desination file path and open to write extracted pdf data
        dest_path = dest_dir + pdf_file 
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


main()