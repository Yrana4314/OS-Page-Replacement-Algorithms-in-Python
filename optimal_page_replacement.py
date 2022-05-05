'''Optimal page replacement algorithm (OPT or OPR) implementation in python
Yogesh Rana'''
# replace a page that willnot be used (requested) by ram for long period of time
from csv import reader

# Total Frame capacity
capacity = 10
# frame list
frame= []
# Page fault counter
fault = 0
# temporary list to store page fault page
page_fault = []
# Temporary list to store the csv data
page_data_list = []
# Open the csv data file as a obj
with open('data_page.csv') as read_obj:
    csv_reader = reader(read_obj)
    # Analyze each row by row
    for row in read_obj:
        # Get rid of the space after the data
        row = row.strip()
        # append to the list
        page_data_list.append(row)

# Create a list of 10 None value
occurance = [None for i in range(capacity)]
# Loop around the total num. of pages
for i in range(len(page_data_list)):
    # if frame has enough memory and page is not in frame
    if page_data_list[i] not in frame:
        if len(frame)<capacity:
            # insert into frame
            frame.append(page_data_list[i])
        else:
            # Loop x around the length of frame
            for x in range(len(frame)):
            # if the page being requested not in page_data_list after i
                if frame[x] not in page_data_list[i+1:]:
                    # replace the page with new page that is not in frame
                    frame[x] = page_data_list[i]
                    break
                else:
                    # store the
                    occurance[x] = page_data_list[i+1:].index(frame[x])
            else:
               frame[occurance.index(max(occurance))] = page_data_list[i]
        # Increment the page fault
        fault += 1
        # append the page fault page to temp page_fault list
        page_fault.append(page_data_list[i])
# Prit the total page requested and Page fault
print(f"Optimal Page replacements' page fault:{page_fault}")
print(f"Total Page Faults: {fault}")
