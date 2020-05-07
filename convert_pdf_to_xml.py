import pdfquery
from lxml import etree
import os

def convert(filename, filepath = ""):
    if filepath:
        pdf = pdfquery.PDFQuery(filepath + "/" + filename)
        pdf.load()
        with open('{}/{}.xml'.format(filepath, filename.replace(".pdf", "")),'wb') as f:
            f.write(etree.tostring(pdf.tree, pretty_print=True))
    else:   
        pdf = pdfquery.PDFQuery(filename)
        pdf.load()
        with open('{}.xml'.format(filename.replace(".pdf", "")),'wb') as f:
            f.write(etree.tostring(pdf.tree, pretty_print=True))


if __name__ == "__main__":
    directory = "resources/Sample files/PDFFiles"
    files = os.listdir(directory)
    #print(files)
    #convert(files[0], directory)
    for file in files:
        convert(file, directory)