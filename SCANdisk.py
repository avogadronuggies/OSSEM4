def scan(n, cylinderpos, start,max):
    left=[cylinder for cylinder in cylinderpos if cylinder<=start]
    right=[cylinder for cylinder in cylinderpos if cylinder>start]
    left.append(0)
    right.append(max)
    left.sort(reverse=True)
    right.sort()

    disk_cylinder= left+right
    total_head=0
    head_movement=[0]*len(disk_cylinder)

    for i in range(len(disk_cylinder)):
            if i ==0:
                   head_movement[i]=abs(start-disk_cylinder[i])
            else:
                head_movement[i]=abs(disk_cylinder[i-1]-disk_cylinder[i])
            total_head+=head_movement[i]

    avgseek = total_head/n
    print("\n-------------------------------------")
    print("|I/O REQUEST\t\tTOTAL HEAD MOVEMENT|")
    print("-------------------------------------")
    for i in range(len(disk_cylinder)):
        print(f"{disk_cylinder[i]}\t\t\t\t\t{head_movement[i]}")
    print("-------------------------------------")
    print(f"AVERAGE SEEK TIME IS : {avgseek}")
    print(f"TOTAL HEAD MOVEMENT: {total_head}")


    
if __name__ == "__main__":
    n_io_requests = int(input("Enter the Number of IO Requests: "))
    if n_io_requests <= 0:
        print("Number of I/O requests should be greater than 0.")
    else:
        cylinder_positions = [0] + list(map(int, input("Enter the Cylinder Nos separated byspace: ").split()))
        start_cylinder = int(input("Enter the Starting Cylinder: "))
        max_cylinder = int(input("Enter the Maximum Cylinder: "))

    print("SCAN")
    scan(n_io_requests, cylinder_positions, start_cylinder, max_cylinder)
