import pdfkit
from PyPDF2 import PdfFileMerger
import os, argparse
def merge_pdfs(input_files: list, page_range: tuple, output_file: str, bookmark: bool = True):
    merger = PdfFileMerger(strict = False)
    for input_file in input_files:
        bookmark_name = os.path.splitext(os.path.basename(input_file))[0] if bookmark else None
        merger.append(fileobj = open(input_file, 'rb'), pages = page_range, import_bookmarks = False, bookmark = bookmark_name)

    merger.write(fileobj = open(output_file, 'wb'))
    merger.close()

regno = 16102113001# enter the starting registration no.

res_link = 'https://akuexam.net/results/ResultsBTechPharm6thSemPub19.aspx?Sem=VI&RegNo=' # enter the result link without registration no.

regno_list = []
for i in range(0,32): # enter the result range
    regno_list.append(regno)
    regno = regno + 1


regno_le = []
regno_le_var = 17102113901 # enter the starting registration no. of le students, if any. if none comment out relevant portions

for i in range (0, 4): # enter the range for the le students
    regno_le.append(regno_le_var)
    regno_le_var = regno_le_var + 1


regno_list = regno_list + regno_le
regno_list.append(15102113033)
regno_list.append(16102113904)
regno_list.sort()


string_regno = [str(x) for x in regno_list]
regno_link = [res_link + x for x in string_regno]

res = [regno_link, string_regno]
regno_pdf = [x + '.pdf' for x in string_regno]


for i in range(len(regno_link)):
    if os.path.exists(regno_pdf[i]):
        continue
    else:
        pdfkit.from_url(regno_link[i], regno_pdf[i])
        print(f'{regno_pdf[i]} has been downloaded')
        i = i + 1




pdfs = regno_pdf
pdfs.sort()
merge_pdfs(input_files=pdfs, page_range = (0,1), output_file = '2k16_me_6th_sem.pdf') # enter the name for the output file in the output_file argument

remf = regno_pdf
for f in remf:
    os.remove(f)
