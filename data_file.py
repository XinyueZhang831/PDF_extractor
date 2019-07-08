import io
import pandas as pd
import csv
import json

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        counter= 0
        counter_back = 2
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()
        #print(text)
        change_to_df(text)

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text


def change_to_df(text):
    array1 = text.split(' ')
    counter  = 0
    while array1[counter] != '1969' :
        counter += 1
    print(counter)
    new_array = []
    i = counter
    while i < len(array1):
        #print(array1[i])
        new_array.append(array1[i: i+10])
        i +=10
    write_to_file(new_array)


def write_to_file(new_array):
    with open('your_file.txt', 'w') as f:
        for item in new_array:
            item = [w.replace(',', '') for w in item]
            f.write("%s\n" % (',').join(item))


def write_to_file1(new_array):
    with open('your_file.txt', 'w') as f:
        i = 1969
        for item in new_array:
                item = [w.replace(',', '') for w in item]
                #print(item)
                item = ('').join(item[:-18])
                print(item)
                f.write("%s\n" % (str(i) +',' + item))
                i +=1


extract_text_from_pdf('/Users/xinyue/PycharmProjects/Work/Clark County Population.pdf')