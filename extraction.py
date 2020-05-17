import pdfquery

pdf = pdfquery.PDFQuery("centrecom-po.pdf")
pdf.load()

x0 = 229 
y0 = 853 - 197 #656
x1 = 286
y1 = 853 - 179 #674


value = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (x0, y0, x1, y1)).text()

print("Vendor num : ")
print(value)



x0 = 53
y0 = 853 - 525
x1 = 186
y1 = 853 - 349


value = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' % (x0, y0, x1, y1)).text()

print("SKUs : ")
print(value)



