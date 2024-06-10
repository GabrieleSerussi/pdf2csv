import pdfplumber
import csv

pdf_name = "L2-ProblemSolving.pdf"
csv_filename = f'{pdf_name.removesuffix(".pdf")}.csv' #"AI2.csv"

with pdfplumber.open(pdf_name) as pdf:
    pages = pdf.pages
    s = ""
    for page in pages:
        s+= page.extract_text()
    l = s.split()
    d = {}
    for word in l:
        d[word] = d.setdefault(word, 0)+1
    #out = sorted(list(d.items()), key= lambda x:x[1], reverse=True)

    #csv_columns = ["word", "occurances"]
    with open(csv_filename, 'w') as csvfile:
        writer = csv.writer(csvfile)#, fieldnames=csv_columns)
        #writer.writeheader()
        #for data in list(d.items()):
        #    writer.writerow(data)
        writer.writerows(d.items())
    print("Done")
