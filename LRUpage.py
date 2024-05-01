

def lru(pages,n):
    page_fault=0
    frames=[]
    last_used={}
    time=0
    for page in pages:
        if page not in frames:
            page_fault+=1
            if len(frames)==n:
                replace_page=min(frames,key=last_used.get)
                replace_index=frames.index(replace_page)
                frames[replace_index]=page
                del last_used[replace_page]
            else:
                frames.append(page)
            last_used[page]=time
        else:
            last_used[page]=time
        time+=1
        print(time)
        print(frames)
    return page_fault


page = list(map(int,input("Enter page referneces separated by spaces:").strip().split()))
n = int(input("Enter the nunber of frames:"))

print("lru Page Replacement:\n")
faults=lru(page,n)
print("Number of page faults:",faults)
