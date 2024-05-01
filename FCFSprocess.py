print("FCFS Process Scheduling")
n = int(input("Enter the number of processes: "))
d = dict()

for i in range(n):
    key = "P" + str(i + 1)
    at = int(input("Enter Arrival time of the process " + str(i + 1) + ": "))
    bt = int(input("Enter Burst time of the process " + str(i + 1) + ": "))
    d[key] = [at, bt]

d = sorted(d.items(), key=lambda item: item[1][0])
ET = []
for i in range(len(d)):
    if i == 0:
        ET.append(d[i][1][1])
    else:
        ET.append(ET[i - 1] + d[i][1][1])

TAT = []
for i in range(len(d)):
    TAT.append(ET[i] - d[i][1][0])

WT = []
for i in range(len(d)):
    WT.append(TAT[i] - d[i][1][1])

avg_WT = sum(WT) / n
avg_TAT = sum(TAT) / n

print("Process | Arrival | Burst| Finish | TurnAround | Waiting")
for i in range(n):
    print(f" {d[i][0]} | {d[i][1][0]} | {d[i][1][1]} | {ET[i]} | {TAT[i]} | {WT[i]}")
print(f"Avg.TAT: {avg_TAT} ms")
print(f"Avg.WT: {avg_WT} ms")

gantt_chart = ""
for i in range(len(d)):
    if i==0:
        ET.append(d[i][1][1])
        gantt_chart += str(d[i][1][0]) + "---" + d[i][0] + "---" + str(ET[i]) + "|"
    else:
        ET.append(ET[i - 1] + d[i][1][1])
        gantt_chart += "---" + d[i][0] + "---" + str(ET[i]) + "|"
print("\nGantt Chart: ")
print(gantt_chart)
