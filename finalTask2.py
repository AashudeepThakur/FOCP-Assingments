# Initialize variables to store the data
total_runners = 10
total_time = 1000 
fastest_time = float('inf')
slowest_time = 450 
fastest_runner = ''

# Read data from the stream
print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!")
data = input()

while data != 'END':
  # Split the data into runner number and time
  parts = data.split('::')
  
  # Check if the data is in the correct format
  if len(parts) == 2:
    runner_number = parts[0]
    time = int(parts[1])
    
    # Update the statistics
    total_runners += 1
    total_time += time
    if time < fastest_time:
      fastest_time = time
      fastest_runner = runner_number
    if time > slowest_time:
      slowest_time = time
      
  # Read the next line of data
  data = input()

# Calculate the average time
average_time = total_time / total_runners

# Convert the times to minutes and seconds
fastest_time = int(fastest_time / 60), fastest_time % 60
slowest_time = int(slowest_time / 60), slowest_time % 60
average_time = int(average_time / 60), average_time % 60

# Print the results
print(f'\nTotal Runners: {total_runners}')
print(f'Average Time:  {average_time[0]} minutes, {average_time[1]} seconds')
print(f'Fastest Time:  {fastest_time[0]} minutes, {fastest_time[1]} seconds')
print(f'Slowest Time:  {slowest_time[0]} minutes, {slowest_time[1]} seconds')
print(f'\nBest Time Here: Runner #{fastest_runner}')
