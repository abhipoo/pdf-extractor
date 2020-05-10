import pdfquery
from lxml import etree
import os
import traceback

def convert(filename, filepath = ""):
    try:
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
    except:
        print(traceback.format_exc())

if __name__ == "__main__":
    #directory = "resources/Sample files/PDFFiles"
    directory = input("Enter directory path containing PDF files [default : Enter] : ")
    print(directory)
    
    while(True):
        bulk_flag = input("Convert all files in this directory (Y [default : Enter]/ N) ? : ").upper()
        
        if bulk_flag == "Y" or bulk_flag == "":
            if directory:
                files = os.listdir(directory)
            else:
                files = os.listdir()

            for filename in files:
                if filename.lower().endswith('.pdf'):
                    print("Converting file :" + filename)
                    convert(filename, directory)
            break
        elif bulk_flag == "N":
            filename = input("Please enter PDF filename to be converted : ")

            if filename.lower().endswith('.pdf'):
                convert(filename, directory)
            else:
                convert(filename + ".pdf", directory)
            break
        else:
            print("Please choose either Y [Enter] / N to continue..")

