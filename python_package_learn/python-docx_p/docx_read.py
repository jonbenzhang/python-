from docx import Document

"""
打开文档
"""
# 方式１
document = Document('existing-document-file.docx')

# 方式2
f = open('foobar.docx', 'rb')
document2 = Document(f)