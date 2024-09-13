import os

files = os.listdir('img')
i = 1
for file in files:
    if file.endswith('.png'):
        os.rename(f"img/{file}", f"img/{i}.png")
        i += 1
