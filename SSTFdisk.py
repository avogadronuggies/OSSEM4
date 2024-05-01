def sstf(n_io_requests, cylinder_positions, start_cylinder):
    disk_cylinders = cylinder_positions[:]
    total_head_movement = 0
    head_movements = [0] * (n_io_requests + 1)
    for i in range(1, n_io_requests + 1):
        min_distance = float('inf')
        min_index = -1
        for j in range(1, n_io_requests + 1):
            if disk_cylinders[j] != -1:
                distance = abs(disk_cylinders[j] - start_cylinder)
                if distance < min_distance:
                    min_distance = distance
                    min_index = j
        head_movements[i] = min_distance

        total_head_movement += min_distance
        start_cylinder = disk_cylinders[min_index]
        disk_cylinders[min_index] = -1
        
    avg_seek_time = total_head_movement / n_io_requests
    print("\n-------------------------------------")
    print("|I/O REQUEST\t\tTOTAL HEAD MOVEMENT|")
    print("-------------------------------------")
    for i in range(1, n_io_requests + 1):
        print(f"{start_cylinder}\t\t\t\t\t{head_movements[i]}")
    print("-------------------------------------")
    print(f"AVERAGE SEEK TIME IS : {avg_seek_time}")
    print(f"TOTAL HEAD MOVEMENT: {total_head_movement}")

if __name__ == "__main__":
    n_io_requests = int(input("Enter the Number of IO Requests: "))
    if n_io_requests <= 0:
        print("Number of I/O requests should be greater than 0.")
    else:
        cylinder_positions = [0] + list(map(int, input("Enter the Cylinder Nos separated byspace: ").split()))
        start_cylinder = int(input("Enter the Starting Cylinder: "))
        max_cylinder = int(input("Enter the Maximum Cylinder: "))

    print("SSTF")
    sstf(n_io_requests, cylinder_positions, start_cylinder)
