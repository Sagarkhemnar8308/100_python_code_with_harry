# a=open('file.txt','r')
# text=a.read()
# print(text)
# a.close()



# b=open('file2.txt','w')
# txt=b.write("hello world")


# with open('file2.txt','a') as p:
#     p.write('egergecferferf')
    
    
    #readline()

with open('file.txt','r') as f:
    f.seek(10)
    data=f.read(5)
    print(data)