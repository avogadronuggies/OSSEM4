
def worstfit(memoryblocks,process_size):
    allocation=[]
    for process in process_size:
        worst_block= None
        max_remaining=0
        for i, block in enumerate(memory_blocks):
            if block>=process and block-process>max_remaining:
                worst_block=i
                max_remaining = block-process

        if worst_block is not None:
            allocation.append((process,worst_block))
            memory_blocks[worst_block]-=process

    for size, block in allocation:
        print(f"Process Size: {size} -> Block No: {block}")

memory_blocks = list(map(int, input("Enter memory block sizes separated by space:").split()))
process_size = list(map(int, input("Enter process sizes separated by space:").split()))

print("\nWorst Fit Allocation:")
worstfit(memory_blocks,process_size)
    
