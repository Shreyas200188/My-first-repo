def nextpoint(x,y):
	if(x>=0 and y>=0):
		if(x<y):
			nextx=x+1
			nexty=y
		else:
			nextx=x
			nexty=y-1
	if(x>0 and y<0):
		if(x<=-y):
			nextx= x-1
			nexty=y
		else:
			nextx=x
			nexty=y-1 
	if(x<=0 and y<=0):
		if(-x<-y):
			nextx= x-1
			nexty=y
		else:
			nextx= x
			nexty=y+1
	if(x<0 and y>0):
		if(-x<y):
			nextx= x+1
			nexty=y
		else:
			nextx= x
			nexty=y+1
	cordinates=(nextx , nexty)
	return cordinates

def prevpoint(x,y):
	if(x>=0 and y>=0):
		if(x<y):
            		print("The previous point is: ", x-1, ",",y)
		else:
            		print("The previous point is: ", x,",",y+1)
	if(x>0 and y<0):
		if(x<=-y):
			print("The previous point is: ", x+1, ",",y)
		else:
			print("The previous point is: ", x, ",",y+1) 
	if(x<=0 and y<=0):
		if(-x<-y):
			print("The previous point is: ", x+1, ",",y)
		else:
			print("The previous point is: ", x, ",",y-1)
	if(x<0 and y>0):
		if(-x+1<y):
			print("The previous point is: ", x-1, ",",y)
		else:
			print("The previous point is: ", x, ",",y-1)

def cspiral(x,y):
	flag=0
	m=0
	n=1
	count=1
	while(flag != 1):
		if(m==x and n==y):
			flag=1
		else:
			newcordinates=nextpoint(m,n)
			m=newcordinates[0]
			n=newcordinates[1]
			count+=1
	return count



print("This program  is the mid-sem project of group 4 and the program is written by Vansh Rai Saini [ID:2019ume0200] \b\b") 
print("This program asks you to enter the cordinates of a point of your choice and it returns the cordinates of the next and the previous point on the spiral.")
print("It also tells you the point number in that spiral\b\b") 
a=int(input("Enter the x cordinate: "))
b=int(input("Enter the y cordinate: "))
newcordinates=nextpoint(a,b)
print("The next point is ",newcordinates[0],",",newcordinates[1])
prevpoint(a,b)
num=cspiral(a,b)
print("The point number is: ",num)
    		

