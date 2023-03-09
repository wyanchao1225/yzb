from docx import Document
#from docx.document import Document as Doc
doc = Document('Chin3500words.docx') # type: Doc
for no, p in enumerate(doc.paragraphs):
     print(no+1,(p.text).split())

