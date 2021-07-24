#這是while loop的練習
x = 0
while x < 10:
	x += 1 #x = x + 1 
	print('我還在迴圈內')
	print('我困在框框裡')
print('我出來了')

#while 後面接是非題>> while true
y = 0
while True:
    if y > 10:
    	break
    elif y <= 10:
    	print('我困住了')
    	y += 1
    	