'''FIFO Page Replacement Algorithms in Python
 By Yogesh Rana'''
 # Total Frame capacity
capacity = 10
# frame list
frame= []
# Page fault counter
fault = 0
# First requested string's index in frame list
top = 0
# Flag page request
pf ='No'
print("Enter the reference string: ",end="")
s = list(map(int,input().strip().split()))
print("\nInput String|Frame →\t",end='')
for i in range(1,capacity+1):
    print(i,end="   ")
#print(*range(1, capacity +1),end="  ")
print("\t Page Fault\n   ↓\n")
for i in s:
    # Loop around the frame
    if i not in frame:
        # Check if the frame size is less than frame's capacity
        if len(frame)<capacity:
            # If the frame is empty, just append the string into frame
            frame.append(i)
        else:
            # Displace the oldest string with new String
            frame[top] = i
            # increment the top index i.e. 2nd oldest string in the frame
            top = (top+1)%capacity
        # Increment the fault counter
        fault += 1
        # Flag the page request as page fault = "Yes"
        pf = 'Yes'
    else:
        pf = 'No'
    print(f"   {i}\t\t\t",end='')
    # Print the page from the frame
    for x in frame:
        print(x,end="  ")
    # Space after printig pages from frame
    for x in range(capacity-len(frame)):
        print("  ",end=' ')
    # Flag the page Fault
    print(f" \t\t{pf}")
# Prit the total page requested and Page fault
print(f"\nTotal requests: {len(s)}\nTotal Page Faults: {fault}")
