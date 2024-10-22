import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Step 1: Load the CSV file
file_path = '/home/alessandro/Documentos/ITA/tese/coletas/coleta_seq3.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Step 2: Clean the data


# Step 3: Convert the timestamp to a datetime format
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Step 4: Normalize the timestamp to start at second 0
start_time = data['timestamp'].min()  # Get the minimum timestamp
data['normalized_time'] = (data['timestamp'] - start_time).dt.total_seconds()  # Normalize to seconds


# Function to calculate mean, median, mode, and standard deviation
def calculate_stats(column):
    mean_val = column.mean()
    median_val = column.median()
    mode_val = stats.mode(column)[0]  # Using scipy's mode function
    std_dev = column.std()

    print(f"Mean: {mean_val}")
    print(f"Median: {median_val}")
    print(f"Mode: {mode_val}")
    print(f"Standard Deviation: {std_dev}")

calculate_stats(data['rxkB/s'])

# Step 5: Create the line plot
plt.figure(figsize=(12, 6))
plt.plot(data['normalized_time'], data['rxkB/s'], linestyle='-', color='b')
plt.title('Data Reception Rate Over Time')
plt.xlabel('Time (seconds from start)')
plt.ylabel('Received Data (kB/s)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()

# Step 6: Show or save the plot
plt.show()  # To display the plot
plt.savefig('coleta_m0.png')  # To save the plot as an image
