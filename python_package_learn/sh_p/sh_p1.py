import sh
a = sh.ls("-l", "/tmp", color="yes")
print(a)
