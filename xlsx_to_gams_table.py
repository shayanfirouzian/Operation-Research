import pandas as pd
file="C:\\Users\\Asus\\Desktop\\ho(j,t).xlsx"

df = pd.read_excel(file, header=None)
k=0

table_name='example'
index1='k'
index2='t'

full_name='table '+table_name+'('+index1+','+index2+')'

with open('C:\\Users\\Asus\\Desktop\\example.txt', 'wb') as f:
    f.write(bytes(full_name , 'utf-8'))
    f.write(bytes('\n', 'utf-8'))
    f.write(bytes('     ', 'utf-8'))
    for j in range(df.shape[1]):
        f.write(bytes(str(j+1), 'utf-8'))
        if j != df.shape[1] - 1:
            f.write(bytes('    ', 'utf-8'))
    f.write(bytes('\n', 'utf-8'))    
    for i in range(df.shape[0]):
        if k==0:
            f.write(bytes('1    ','utf-8'))
            k=k+1
        for j in range(df.shape[1]):
            value = str(df.iloc[i, j])
            f.write(bytes( value , 'utf-8'))
            if i == df.shape[0] - 1 and j == df.shape[1] - 1:
                f.write(bytes(';\n', 'utf-8'))
            elif j == df.shape[1] - 1:
                f.write(bytes('\n', 'utf-8'))
                f.write(bytes(str(i+2)+'    ','utf-8'))
            else:
                f.write(bytes('    ', 'utf-8'))    

