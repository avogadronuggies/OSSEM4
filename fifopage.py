
def fifo(pages,n):
    page_fault=0
    frames=[]
    replace_index = 0
    for page in pages:
        if page not in frames:
            page_fault+=1
            if len(frames)==n:
                frames[replace_index]=page
                replace_index = (replace_index+1)%n
            else:
                frames.append(page)
        else:
            pass
        print(frames)
    return page_fault
                

page = list(map(int,input("Enter page referneces separated by spaces:").strip().split()))
n = int(input("Enter the nunber of frames:"))

print("FIFO Page Replacement:\n")
faults=fifo(page,n)
print("Number of page faults:",faults)
