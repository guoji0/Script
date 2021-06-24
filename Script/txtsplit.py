import re
with open ('/home/guo/script2/cppcheck_202105181409.txt','r') as file:
    if file:
        f = file.read()
        lineList = f.split( '^')
        total_list = []
        for line in lineList:
            if lineList.index(line) != len(lineList)-1:
                print(lineList.index(line))
                print(line)
                line_list = []
                line_list.append(line.split(':')[0])
                line_list.append(line.split(':')[1])
                line_list.append(line.split(':')[2])
                line_list.append(line.split(':')[3])
                #print(re.search(r':*.?',line).group())
            #alist = re.split('[:.]',line)
            #total_list.append(line)
        #print(total_list[0])