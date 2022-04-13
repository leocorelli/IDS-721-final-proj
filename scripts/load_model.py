import pickle

def load_model(path: str):
    file = open(path,'rb') # path is where .pkl file is saved
    model = pickle.load(file) 
    return model