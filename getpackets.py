import os

link = "https://science.energy.gov/~/media/wdts/nsb/pdf/HS-Sample-Questions/Sample-Set-%s/round%s.pdf"
link2 = "https://science.energy.gov/~/media/wdts/nsb/pdf/HS-Sample-Questions/Sample-Set-%s/Sample%s_ROUND%s.pdf"
link3 = "https://science.energy.gov/~/media/wdts/nsb/pdf/HS-Sample-Questions/Sample-Set-%s/ROUND-%sC.pdf"
link8 = "https://science.energy.gov/~/media/wdts/nsb/pdf/HS-Sample-Questions/Sample-Set-%s/Round-%s-A.pdf"
link9 = "https://science.energy.gov/~/media/wdts/nsb/pdf/HS-Sample-Questions/Sample-Set-%s/RegionalHS_%sA.pdf"
link10 = "https://science.energy.gov/~/media/wdts/nsb/pdf/HS-Sample-Questions/Sample-Set-%s/%sA_HS_Reg_2016.pdf"

pkts = []

'''

#example

for s in range(2,3):
	s = s+1
	if s==3:
		for r in range(17):
			r = r+1
			os.system("wget " + link3 % (s, r) + " -O ./pkts/round%s-%s.pdf " % (s, r) + "--no-check-certificate")
			pkts.append("./pkts/round%s-%s.pdf" % (s, r))

'''

for s in range(10):
	s = s+1
	if s in [5,6]:
		for r in range(15):
			r = r+1
			pkts.append("./pkts/round%s-%s.pdf" % (s, r))
	else:
		for r in range(17):
			r = r+1
			pkts.append("./pkts/round%s-%s.pdf" % (s, r))

from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader

pdfWriter = PdfFileWriter()
'''
for pkt in pkts:
	pdfFileObj = open(pkt, "rb")
	pdfReader = PdfFileReader(pdfFileObj)
	for pageNum in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)

pdfOutput = open('result.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
'''
pdfFileObj = open('result.pdf', 'rb')
pdfReader = PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())


