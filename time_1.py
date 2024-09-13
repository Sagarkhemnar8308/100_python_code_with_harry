import time as tm
timestamp = tm.strftime('%H:%M:%S')
hr = int(tm.strftime('%H'))
print(hr)

if(hr >= 0  and hr <= 12):
    print("Good Morning 😍")
elif(hr >= 1 and hr <= 16):
    print("Good Afternoon ��")
elif(hr >= 17 and hr <= 21):
    print("Good Evening ��")
else:
    print("Good Night ................................")

