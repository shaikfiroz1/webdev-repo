import csv

# data = [{"name": "Alice", "score": 92}, {"name": "Bob", "score": 85}]

# with open ("context.csv", "w", newline="", encoding="utf-8 ") as f :

#     writer=csv.DictWriter(f, fieldnames=["name", "score"])
#     writer.writeheader()
#     writer.writerows(data)




with open ("context.csv", "r",  encoding="utf-8 ") as f :

    writer=csv.DictReader(f)
    for line in writer : 
        print(line["name"], line ["score"])