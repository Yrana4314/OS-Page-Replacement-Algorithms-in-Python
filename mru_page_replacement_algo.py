'''MRU page replacement algorithm implementation in python
By Yogesh Rana'''

from csv import reader
def mru():
    # Total Frame capacity
    capacity = 10
    # frame list
    frame= []
    # Page fault counter
    fault = 0
    # Page fault page list
    page_fault_list = []
    # list to track the insertion of the page into frame
    # We can call it index list
    str = []
    # Open the csv data file
    with open('data_page.csv') as read_obj:
        #csv_reader = reader(read_obj)
        # Analyze each row by row
        for page in read_obj:
            # Get rid of the space before & after the data from CSV file
            page = page.strip()
            # check if requested page doesn't exist in frame
            if page not in frame:
                # if frame size is less than capacity i.e. 10
                if len(frame)<capacity:
                    # Append page into frame
                    frame.append(page)
                    # Append one less sie of frame into str list
                    str.append(len(frame)-1)
                else:
                    # Remove the last index from str list AND
                    # Assign to index variable
                    index = str.pop()
                    # Append the page in the index variable position
                    frame[index] = page
                    # Append that index at the end of the str list
                    str.append(index)
                # Append the page that flag page fault to
                page_fault_list.append(page)
                #pf = 'Yes'
                # Increment page fault counter
                fault += 1
            else:
                # if the requested page is already present in the frame list
                # first, Find the index of that page in frame,
                # second, find the index of the index of that page in str list
                # Third remove that index from str list
                # Append that index at last of the str list
                str.append(str.pop(str.index(frame.index(page))))

    print(page_fault_list)
    print(f"\nTotal Page Faults: {fault}")

if __name__ == "__main__":
    mru()


