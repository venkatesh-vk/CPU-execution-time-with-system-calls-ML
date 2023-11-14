import pandas as pd
import random

# Load your existing dataset
existing_data = pd.read_csv('SCE2.csv')

# Number of new data points to generate
num_new_data_points = 5000 - len(existing_data)

# Initialize an empty list to store the new data
new_data = []

# Define a range for random variations
variation_range = 5  # You can adjust this as needed

# Generate new data points
for _ in range(num_new_data_points):
    # Randomly select an existing data point to use as a base
    base_data_point = existing_data.sample()

    # Create a new data point by adding random variations
    new_data_point = base_data_point.copy()

    for column in existing_data.columns:
        if column != 'File' and column != 'CPU Time (seconds)':
            variation = random.randint(-variation_range, variation_range)
            new_data_point[column] += variation

    # Append the new data point to the list
    new_data.append(new_data_point)

# Concatenate the existing data with the new data
synthetic_data = pd.concat([existing_data] + new_data, ignore_index=True)

# Save the synthetic data to a new CSV file
synthetic_data.to_csv('synthetic_dataset2.csv', index=False)
