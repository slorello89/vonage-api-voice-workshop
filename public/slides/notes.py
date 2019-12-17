import sys
import PyPDF2, traceback

try :
    src = sys.argv[1]
except :
    src = r'/path/to/my/file.pdf'

# put the role into the rst file
print '.. role:: slide-title'
print ''

input1 = PyPDF2.PdfFileReader(open(src, "rb"))
nPages = input1.getNumPages()

for i in range(nPages) :
    page0 = input1.getPage(i)
    text = page0.extractText()
    print ':slide-title:`' + text.splitlines()[0] + '`'
    print ''
    try :
        for annot in page0['/Annots'] :
            print(annot.getObject()['/Contents'])
            print ''
    except : 
        # there are no annotations on this page
        pass

    print ''
