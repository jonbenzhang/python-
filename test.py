while True:
    try:
        a = input("")
        results = []
        result = ""
        left = 0
        sign = True
        for i in range(len(a)):
            if a[i] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
                if sign:
                    left = i
                    sign = False
            else:
                if not sign:
                    if i - left == len(result):
                        result = a[left:i]
                        results.append(result)
                    elif i - left > len(result):
                        results = []
                        result = a[left:i]
                        results.append(a[left:i])
                    sign = True
        print("".join(results), len(result))

    except:
        break