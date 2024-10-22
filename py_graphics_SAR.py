import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Step 1: Load the CSV file
file_path = '/home/alessandro/Documentos/ITA/tese/coletas/coleta_seq3.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Step 2: Clean the data
#data['rxkB/s'] = data['rxkB/s'].str.replace(',', '.').astype(float)

# Step 3: Convert the timestamp to a datetime format
# This is where we convert the timestamp format
def convert_timestamp(original_timestamp):
    # Parse the original timestamp and convert to the desired format
    date_object = datetime.strptime(original_timestamp, "%Y-%m-%d %H:%M:%S %Z")
    return date_object.strftime("%m/%d/%Y %H:%M:%S %Z")

data['timestamp'] = data['timestamp'].apply(convert_timestamp)

# Step 4: Convert the formatted timestamp back to datetime for plotting
data['timestamp'] = pd.to_datetime(data['timestamp'], format="%m/%d/%Y %H:%M:%S %Z")

# Step 5: Normalize the timestamp to start at second 0
start_time = data['timestamp'].min()  # Get the minimum timestamp
data['normalized_time'] = (data['timestamp'] - start_time).dt.total_seconds()  # Normalize to seconds

# Step 6: Create the line plot
plt.figure(figsize=(12, 6))
plt.plot(data['normalized_time'], data['rxkB/s'], marker='o', linestyle='-', color='b')
plt.title('Data Reception Rate Over Time (Normalized)')
plt.xlabel('Time (seconds from start)')
plt.ylabel('Received Data (kB/s)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()

# Step 7: Show or save the plot
plt.show()  # To display the plot
# plt.savefig('data_reception_rate.png')  # To save the plot as an image
