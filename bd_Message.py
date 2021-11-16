
# file = open('./old/text', 'r')

# TWG = file.read()

start = '<div class="im-mess--text wall_module _im_log_body">'
end = '</div>'

def SearchDiv(text, divS, divE):
    arrayOfDivs = []
    while len(text) > 0:
        indexS = text.find(divS)
        indexE = text.find(divE)
        message = text[indexS+len(divS):indexE]
        text = text[indexE + 6:len(text)]
        if message == '':
            continue
        if not message.find("<div") or not message.find("<img") or not message.find('<a') or not message.find("href"):
            continue
        arrayOfDivs.append(message)
        if not text.rfind(divS):
            break
    return arrayOfDivs


def clearDivs(text):
    line = text.readline()
    arrayOfStr = []
    while line:
        indexD = line.find("<div")
        indexS = line.find("<span")
        indexI = line.find("<img")
        indexA = line.find("<a ")
        if indexD > 0:
            line = line[0:indexD] + '\n'
        elif indexS > 0:
            line = line[0:indexS] + '\n'
        elif indexI > 0:
            line = line[0:indexI] + '\n'
        elif indexA > 0:
            line = line[0:indexA] + '\n'
        arrayOfStr.append(line)
        line = text.readline()
    return arrayOfStr


file = open('reuslt', 'r')

result = clearDivs(file)

file.close()

file = open('reuslt', 'w+')

file.write(''.join(result))

'''
array = SearchDiv(TWG, start, end)
print(array)
file.close()

file = open('reuslt', 'w')

inText = ''
for item in array:
    inText += item + '\n'
file.write(inText)
file.close()
'''



if __name__ == '__main__':
    a = 1
