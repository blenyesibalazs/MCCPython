import json
import csv

# Open input and output files
with open('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/Data/SNP500.json', 'r') as f_input, open('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/Data/SNP500output_2003_2023.csv', 'w', newline='') as f_output:
    # Load JSON data
    data = json.load(f_input)

    # Extract data
    trades = data['md_get_history_response']['trades']
    fields = ['date', 'last']
    rows = [{'date': trade['date'], 'last': trade['last']} for trade in trades]
    
    # Write to CSV
    writer = csv.DictWriter(f_output, fieldnames=fields)
    
    writer.writeheader() 
    writer.writerows(rows)