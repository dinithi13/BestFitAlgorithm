# Initial Block Sizes and Processes
blocks = [150, 500, 300, 100, 200]# List of block sizes
processes = [('A', 90), ('B', 200), ('C', 400), ('D', 150), ('E', 70)] # List of processes (name, size)
allocated = [None] * len(blocks)  # To track which blocks have been allocated


def best_fit(blocks, processes):
     # Iterate over each process to allocate it to a block
    for process_name, process_size in processes:
        best_fit_index = -1 # Variable to store the best block index
        best_fit_remaining = float('inf')  # Start with an infinitely large remaining space

        # Check each block to find the best fit for the process
        for i in range(len(blocks)):
            if allocated[i] is None:  # Block is not yet allocated
                remaining_space = blocks[i] - process_size # Calculate remaining space in block
                if remaining_space >= 0 and remaining_space < best_fit_remaining: # Check if it fits better than the previous best fit
                    best_fit_index = i # Update the best fit block index
                    best_fit_remaining = remaining_space # Update the best fit remaining space

       
        # If a block was found, allocate the process to that block
        if best_fit_index != -1:
            allocated[best_fit_index] = (process_name, process_size)  # Mark block as allocated
            blocks[best_fit_index] -= process_size  # Update remaining space in block

        else:
            print(f"Process {process_name} could not be allocated. No sufficient space left.") # If no block is found, print a message

# Call the function to allocate processes to blocks
best_fit(blocks, processes)

# Display the final block status
print("\n+------------+--------------------+------------------------+--------------------+")
print("| Block No.  | Original Size (KB) | Process (Name:Size)    | Remaining Size (KB)|")
print("+------------+--------------------+------------------------+--------------------+")
for i in range(len(blocks)):
    process_info = allocated[i] if allocated[i] else ('Not Allocated', '') # Get process info or 'Not Allocated' if none
    # Combine process name and size
    process_name_size = f"{process_info[0]}:{process_info[1]}KB" 
    # Adjust the width of columns, making sure all parts are aligned
    print(f"| {i + 1:<10} | {150 if i == 0 else 500 if i == 1 else 300 if i == 2 else 100 if i == 3 else 200 :<18} | {process_name_size:<22} | {blocks[i]:<18} |")
print("+------------+--------------------+------------------------+--------------------+")

