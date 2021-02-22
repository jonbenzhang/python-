from docx import Document

"""
打开文档
"""
# 方式１
document = Document('zhangbei.docx')
catalog_list = []
catalog_tree = []
for p in document.paragraphs:
    style_name = p.style.name
    if style_name.startswith('Heading'):
        level = style_name.split()[1]
        catalog_list.append([level, p.text])
        # print(level)
        # print(p.text)
        # print(style_name, p.text, sep=':')
l = 0
for level, name in catalog_list:
    level = int(level)
    children = catalog_tree
    if not l:
        l = level
    for _ in range(level - l):
        children = catalog_tree[-1]["children"]
    children.append({"name": name, "children": []})


print(catalog_tree)
import json
print(json.dumps(catalog_tree, ensure_ascii=False))
