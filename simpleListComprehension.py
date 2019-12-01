list_number = [100, 132,345,678,987,675,4578,9865,789]

new_list = [num/10 for num in list_number]

print(new_list)

sensor_readings= [10,80,-56,90,-89,-70,30]

updated_readings =[readings for readings in sensor_readings if readings>0]

print(updated_readings)