i = int ( input("Enter No. of Row: ") )
j = int ( input("Enter No. of Column: ") )

a=[]
for r_i in range(0,i):
    a.append([])
    for c_i in range(0,j):
        a[r_i].append(int())

for r_i in range(0,i):
    for c_i in range(0,j):
        a[r_i][c_i] = int( input("Enter the Value: ") )


r_i = 0
while r_i<i:
	c_i=0
	while c_i<j:
		print(a[r_i][c_i],end=" ")      # end=" " used to end print statement by ' ' not '\n'
		c_i = c_i+1
	print("\n")
	r_i=r_i+1
