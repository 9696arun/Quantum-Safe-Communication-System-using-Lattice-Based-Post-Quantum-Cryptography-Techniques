import matplotlib.pyplot as plt
import csv

msg_sizes = []
file_sizes = []

with open("analysis/log.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == "MSG":
            msg_sizes.append(int(row[1]))
        elif row[0] == "FILE":
            file_sizes.append(int(row[1]))

# Plot
plt.figure()

plt.hist(msg_sizes, bins=5)
plt.title("Message Size Distribution")
plt.xlabel("Size")
plt.ylabel("Frequency")
plt.show()

if file_sizes:
    plt.figure()
    plt.hist(file_sizes, bins=5)
    plt.title("File Size Distribution")
    plt.xlabel("Size")
    plt.ylabel("Frequency")
    plt.show()