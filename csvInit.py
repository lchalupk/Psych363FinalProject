import csv

header = ['bf1RT', 'bf1A', 'happyRT', 'happyA', 'wf1RT', 'wf1A', 'agonyRT', 'agonyA', 'bf2RT', 'bf2A', 'poisonRT', 'poisonA', 'wf2RT', 'wf2A', 'blissRT', 'blissA', 'bf3RT', 'bf3A', 'loveRT', 'loveA', 'wf3RT', 'wf3A', 'hateRT', 'hateA']
with open('results.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
