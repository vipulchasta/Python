#   * 
#   **
#   ***
#   ****
#   *****

n = int( input("Enter n: ") )

for r_i in range(0,n):
    #print("r_i = ",r_i)
    for c_i in range(0,r_i+1):
        #print(c_i,end="")
        print("* ",end="")
    print("")

input("Enter Any Key to Exit")
