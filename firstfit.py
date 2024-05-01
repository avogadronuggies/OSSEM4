
def firstfit(memoryblocks,process_size):
    allocation=[]
    for i in range(len(process_size)):
        for j in range(len(memoryblocks)):
            if memoryblocks[j]>=process_size[i]:
                allocation.append((i,process_size[i],j))
                memoryblocks[j]-=process_size[i]
                break
    print("Process No\tProcess Size\tBlock No")
    for allocated in allocation:
        print(f"{allocated[0]}\t\t{allocated[1]}\t\t{allocated[2]}")


memory_blocks = list(map(int, input("Enter memory block sizes separated by space:").split()))
process_size = list(map(int, input("Enter process sizes separated by space: ").split()))

print("First fit allocation:")
firstfit(memory_blocks,process_size)
