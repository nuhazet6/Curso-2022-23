with open('prueba.dat','w') as f:
    data = [1,2,3,4,5]
    f.writelines('\n'.join(str(datum) for datum in data))
    f.write('\n')
f = open('prueba.dat','r')
g = open('prueba2.dat','w')
text = f.readlines()
text.append('wololo ')
text.append('wololo\n')
g.writelines(text)