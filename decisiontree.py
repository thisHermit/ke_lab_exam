class Node:
    left, right = None, None
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return str(self.data)

root = Node("status")
left = Node("salary")
right = Node("experience")
root.left = left
root.right = right

import csv
# function to get dataset in appropriate format
dataset = []
filename = 'bill_authentication.csv'
with open(filename) as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        if row[0] != 'Variance':
            dataset.append(row)
print(dataset)

# 
def entropy(X, D):
    # for each unique x in X
    # - sum (p(x) * log2(p(x)))
    pass
def info(A, D):
    # for each partition di of A
    # sum((len(di) / len(d)) * entropy(di))
    pass

def gain(A):
    # info(D) - infoA(D)
    pass
