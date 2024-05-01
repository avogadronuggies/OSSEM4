# Banker's Algorithm
 
# Driver code:
if __name__=="__main__":
     
    # P0, P1, P2, P3, P4 are the Process names here
    n = int(input("Enter No.of process:")) # Number of processes
    m = int(input("Enter No. of resources:")) # Number of resources
     
    # Allocation Matrix
    alloc = []
    print("Enter the allocation matrix:")
    for i in range(n):
        temp_list = list(map(int, input().split()))
        alloc.append(temp_list)        
     
    # MAX Matrix
    max = []
    print("Enter the Max matrix:")
    for i in range(n):
        temp_list = list(map(int, input().split()))
        max.append(temp_list)

    avail = list(map(int,input("Enter Available Resources:").split()))  
    f = [0]*n
    ans = [0]*n
    ind = 0
    for k in range(n):
        f[k] = 0

    total_resources = [0]*m
    for j in range(m):
        total_resources[j] += avail[j]+ sum(alloc[i][j] for i in range(n))
    print("Total Resoures:",total_resources)         
    need = [[ 0 for i in range(m)]for i in range(n)]
    print("Need Matrix:\n")
    for i in range(n):
        for j in range(m):
            need[i][j] = max[i][j] - alloc[i][j]
    for i in  range(n):
        for j in range(m):
            print(need[i][j],end=" ")
        print()   
    y = 0
    for k in range(5):
        for i in range(n):
            if (f[i] == 0):
                flag = 0
                for j in range(m):
                    if (need[i][j] > avail[j]):
                        flag = 1
                        break
                 
                if (flag == 0):
                    ans[ind] = i
                    ind += 1
                    for y in range(m):
                        avail[y] += alloc[i][y]
                    f[i] = 1                 
    print("Following is the SAFE Sequence") 
    for i in range(n - 1):
        print(" P", ans[i], " ->", sep="", end="")
    print(" P", ans[n - 1], sep="")
