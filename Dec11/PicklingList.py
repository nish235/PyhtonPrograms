import pickle

l1 = ['a', 'b', 'c', 'd']
with open('datafile.txt', 'wb') as fh:
    pickle.dump(l1, fh)
print("File Write Successfully")
