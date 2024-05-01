def bestfit(memory_blocks, process_size):
    allocation = []
    for process in process_size:
        best_block = None
        min_remaining = float('inf')
        for i, block in enumerate(memory_blocks):
            if block >= process and block - process < min_remaining:
                best_block = i
                min_remaining = block - process
        if best_block is not None:
            allocation.append((process, best_block))
            memory_blocks[best_block] -= process            

    print("Process No\tProcess Size\tBlock No")
    for size, block in allocation:
        print(f"Process Size: {size} -> Block No: {block}")


memory_blocks = list(map(int, input("Enter memory block sizes separated by space:").split()))
process_size = list(map(int, input("Enter process sizes separated by space: ").split()))

print("Best fit allocation:")
bestfit(memory_blocks,process_size)
