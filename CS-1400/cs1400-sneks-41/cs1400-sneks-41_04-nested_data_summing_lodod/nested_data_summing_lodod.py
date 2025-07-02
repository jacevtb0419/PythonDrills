forecast = [
    {"Day": "Friday", "Location": "Blacksburg",
     "Weather": {"Rainfall": 2, "Temperature": 60, "Windy?": False}},
    {"Day": "Saturday", "Location": "Blacksburg",
     "Weather": {"Rainfall": 4, "Temperature": 65, "Windy?": True}},
    {"Day": "Sunday", "Location": "Blacksburg",
     "Weather": {"Rainfall": 1, "Temperature": 72, "Windy?": True}},
]
inches = 0
for day in forecast:
    inches = day["Weather"]["Rainfall"] + inches
print(inches)