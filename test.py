a = {"custom":{},"username":"","capabilities":{"version_control":False,"create_projects":True,"delete_projects":True,"rename_projects":True,"deploy_projects":True,"rename_spiders":True,"rename_templates":True}}
b = {"username":"","capabilities":{"deploy_projects":False,"delete_projects":True,"create_projects":True,"rename_projects":True,"version_control":False,"rename_templates":True,"rename_spiders":True},"custom":{}}
aa = [i for i in a]
aa.sort()
bb = [i for i in b]
bb.sort()
print(aa)
print(bb)
for i,j in a["capabilities"].items():
    if j!=b["capabilities"][i]:
        print(i,j)
