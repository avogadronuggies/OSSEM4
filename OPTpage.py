

def opt(pages,n):
    page_fault=0
    frames=[]
    counter=0
    for page in pages:
        if page not in frames:
            page_fault+=1
            if len(frames)<n:
                frames.append(page)
            else:
                distances=[len(pages)]*n
                for j,frame in enumerate(frames):
                    if frame in pages[counter:]:
                        distances[j]=pages[counter:].index(frame)
                max_distance=distances.index(max(distances))
                frames[max_distance]=page
        else:
            pass
        print(frames)
        counter+=1
    return page_fault
        
    

page = list(map(int,input("Enter page referneces separated by spaces:").strip().split()))
n = int(input("Enter the nunber of frames:"))

print("OPT Page Replacement:\n")
faults=opt(page,n)
print("Number of page faults:",faults)
