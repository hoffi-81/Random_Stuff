import json

# Read data from the text file
with open(r'C:\stations_id.txt', 'r') as file:
    lines = file.readlines()

# Remove leading and trailing whitespaces from each line
cleaned_lines = [line.strip() for line in lines]

# Extract headers
headers = cleaned_lines[0].split()

# Create a list to store station data
station_data = []

# Iterate over the remaining lines and create a dictionary for each station
for line in cleaned_lines[1:]:
    values = line.split()
    station_dict = {header: value for header, value in zip(headers, values)}
    station_data.append(station_dict)

# Convert the list of dictionaries to JSON
json_data = json.dumps(station_data, indent=2)

# Write the JSON data to a file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)
