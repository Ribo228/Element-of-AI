import math
import numpy as np
text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def distance(a,b):
    sum = 0
    for a1,b1 in zip (a,b):
        sum = sum + (a1-b1)**2
    return np.sqrt(sum)

def main(text):
    docs = [line.lower().split() for line in text.split('\n')]
    docsdict = {}
    linedicts = []
    for line in docs:
        linedict = {}
        for word in line:
            if word in linedict.keys():
                linedict[word] += 1
            else:
                linedict[word] = 1
            if word in docsdict.keys():
                docsdict[word] += 1
            else:
                docsdict[word] = 1
        linedicts.append(linedict)
    tf_idf = []
    line_index = 0
    for line in docs:
        line_vector = []
        for word in line:
            line_vector.append(linedicts[line_index][word] * math.log ( 1/docsdict[word]))
        tf_idf.append(line_vector)
        line_index += 1
    outerrow = []
    outerrow_index = 0
    for row in tf_idf:
        innerrow_index = 0
        innerrow = []
        for secondrow in tf_idf:
            if innerrow_index == outerrow_index:
                innerrow.append(np.inf)
            else:
                innerrow.append(distance(row,secondrow))
            innerrow_index += 1
        outerrow.append(innerrow)
        outerrow_index += 1
    dist = np.stack(outerrow)
    print(np.unravel_index(np.argmin(dist),dist.shape))
main(text)



