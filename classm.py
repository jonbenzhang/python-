def a():
    c = 4
    print(eval("c+1",globals(), {"c":6}))
a()