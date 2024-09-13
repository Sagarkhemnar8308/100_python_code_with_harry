import os
if(not os.path.exists('data')):
   os.mkdir('data')

# for i in range(1,101):
#     if(not os.path.exists(f'data/Day{i}')):
#       os.mkdir(f'data/Day{i}')
      
for i in range(1,101):
    os.rename(f'data/tutorial {i}',f'data/Tutorial {i}')
