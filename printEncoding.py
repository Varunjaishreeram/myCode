def printEncoding(string, val,output):

    if string == "":
        print(val)
        output[0]=output[0]+1
        return

    c = len(string)
    for i in range(c):
        first = string[0:i + 1]
        last = string[i + 1:c]
        if first != "":
            if first[0] != "0" and int(first) > 0 and int(first) <= 26:
                printEncoding(last, val + chr(int(first) + 96),output)
    return output
print(printEncoding("11","",[0]))