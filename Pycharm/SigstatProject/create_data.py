import numpy as np
import torch

from torch.utils.data import Dataset, DataLoader

np.random.seed(444)


# data loader for our data set
def data_loader(data, batch_size=6):
    data = SiameseDataSet(data)
    loader = DataLoader(data, batch_size=batch_size)
    return loader


# dataset to iterate through the batches
class SiameseDataSet(Dataset):
    def __init__(self, data):
        self.df = data

    def __len__(self):
        return len(self.df)

    def __getitem__(self, index):
        pair = self.df[index]
        return torch.tensor(pair[0]).float(), torch.tensor(pair[1]).float(), torch.tensor(pair[2]).float()
