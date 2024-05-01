def fcfs(n,cylinderpos,start):
    total_head=0
    head_movement = [0]*(n+1)
    for i in range(n+1):
        if i==0:
            head_movement[i] = abs(start-cylinderpos[i])
        else:
            head_movement[i] = abs(cylinderpos[i-1]-cylinderpos[i])
        total_head += head_movement[i]

    avgseek=total_head/n

    print("\n-------------------------------------")
    print("|I/O REQUEST\t\tTOTAL HEAD MOVEMENT|")
    print("-------------------------------------")
    for i in range(1, n + 1):
        print(f"{cylinderpos[i]}\t\t\t\t\t{head_movement[i]}")
    print("-------------------------------------")
    print(f"AVERAGE SEEK TIME IS : {avgseek}ms")
    print(f"TOTAL HEAD MOVEMENT: {total_head}")
    

if __name__ == "__main__":
    n_io_requests = int(input("Enter the Number of IO Requests: "))
    if n_io_requests <= 0:
        print("Number of I/O requests should be greater than 0.")
    else:
        cylinder_positions = [0] + list(map(int, input("Enter the Cylinder Nos separated byspace: ").split()))
        start_cylinder = int(input("Enter the Starting Cylinder: "))
        max_cylinder = int(input("Enter the Maximum Cylinder: "))

    print("FCFS")
    fcfs(n_io_requests, cylinder_positions, start_cylinder)
