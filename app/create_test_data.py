from travel import travel_options
import json

content = travel_options()
print(content)
with open('test_data.json', 'wb') as file:
    file.write(json.dumps(content).encode())
