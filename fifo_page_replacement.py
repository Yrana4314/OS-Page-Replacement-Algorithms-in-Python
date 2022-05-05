'''FIFO Page Replacement Algorithms in Python
 By Yogesh Rana'''
from csv import reader
 # Total Frame capacity
capacity = 10
# frame list
frame= []
# Page fault counter
fault = 0
# Oldest page's index in frame list
top = 0
# Temporary page fault list to  pages
page_fault = []
# Open the csv data file
with open('data_page.csv') as read_obj:
    csv_reader = reader(read_obj)
    # Analyze each row by row
    for row in read_obj:
        # Get rid of the space before & after the data from CSV file
        row = row.strip()
        if row not in frame:
            # Check if the frame size is less than frame's capacity
            if len(frame)<capacity:
                # If the frame is empty, just append the string into frame
                frame.append(row)
            else:
                # Displace the oldest string with new String
                frame[top] = row
                # increment the top index i.e. 2nd oldest string in the frame
                top = (top+1)%capacity
            # Increment the fault counter
            fault += 1
            # Append to the page_Fault list
            page_fault.append(row)

# Prit the total page requested and Page fault
print(f" FIFO Page fault: {page_fault}")
print(f"Total Page Faults: {fault}")
