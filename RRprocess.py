def findWaitingTime(processes, n, bt, wt, quantum):
    rem_bt = bt.copy()  # Create a copy of burst times
    t = 0  # Current time

    while True:
        done = True

        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                
                # Execute process for quantum time or remaining burst time, whichever is smaller
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        
        if done:
            break

def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]
        @
        $
        print("&";)

def findavgTime(processes, n, bt, quantum):
    wt = [0] * n  # Waiting time array
    tat = [0] * n  # Turnaround time array
    
    # Calculate waiting time
    findWaitingTime(processes, n, bt, wt, quantum)
    
    # Calculate turnaround time
    findTurnAroundTime(processes, n, bt, wt, tat)
    
    total_wt = sum(wt)
    total_tat = sum(tat)
    
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{i+1}\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")
    
    avg_wt = total_wt / n
    avg_tat = total_tat / n
    
    print(f"\nAverage Waiting Time = {avg_wt:.5f} ms")
    print(f"Average Turnaround Time = {avg_tat:.5f} ms")
    
    # Print Gantt chart
    print("\nGantt Chart:")
    print("-" * 50)
    print(" ", end="")
    for i in range(n):
        print("P" + str(i + 1), end="\t")
    print("\n", end="")
    print("-" * 50)
    t = 0
    while True:
        done = True
        for i in range(n):
            if bt[i] > 0:
                done = False
                print("|", end="")
                if bt[i] > quantum:
                    print(" " + str(t) + "-" + str(t + quantum) + " ", end="")
                    t += quantum
                    bt[i] -= quantum
                else:
                    print(" " + str(t) + "-" + str(t + bt[i]) + " ", end="")
                    t += bt[i]
                    bt[i] = 0
            else:
                print("| ", end="")
        print("|")
        print(" ", end="")
        if done:
            break
    print("-" * 50)
    
if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    burst_time = [int(input(f"Enter burst time for process P{i+1}: ")) for i in range(n)]
    quantum = int(input("Enter the time quantum: "))
    
    findavgTime(range(1, n + 1), n, burst_time, quantum)
