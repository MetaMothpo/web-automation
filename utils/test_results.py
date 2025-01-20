import csv
from datetime import datetime

def save_test_result(test_name, status, email=None, password=None):
    with open('test_results.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, test_name, status, email, password]) 