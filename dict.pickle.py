import pickle
inFile = (open('dict.pickle','rb')
newList = pickle.load(infile)
print(newList)
inFile.cloose()

          
