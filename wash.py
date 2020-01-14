import sys, getopt
def wash(filename):
    with open(filename) as fileobj:
        for line in fileobj:
            newline = line.replace('[]','')
            newline = newline.replace('[[[','[')
            newline = newline.replace('[[','[')
            newline = newline.replace(']]]',']')
            newline = newline.replace(']]',']')
    return newline

def normalization(line,filename):
    f = open(filename, "w")
    writeflag = False
    for ch in line :
        if ch == '[' :
            writeflag = True
            f.write('[')
        elif ch == ']' :
            writeflag = False
            f.write('],\n')
        elif writeflag :
            f.write(ch)
        else:
            pass
    f.close()


options,args = getopt.getopt(sys.argv[1:],"i:o:",["input=","output="])


if __name__ == '__main__':
    in_value, out_value = "", ""
    for opt_name,opt_value in options:
        if opt_name in ["-i","--input"]:
            in_value = opt_value
        if opt_name in ["-o","--output"] :
            out_value = opt_value

    if in_value and out_value :
        normalization(line=wash(in_value), filename=out_value)
    else :
        print("you should add -i -o parameter")