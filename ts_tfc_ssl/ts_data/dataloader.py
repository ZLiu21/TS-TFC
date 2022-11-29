import torch
import torch.utils.data as data


class UCRDataset(data.Dataset):
    def __init__(self, dataset, target):
        self.dataset = dataset
        if len(self.dataset.shape) == 2:
            self.dataset = torch.unsqueeze(self.dataset, 1)
        self.target = target

    def __getitem__(self, index):
        return self.dataset[index], self.target[index]

    def __len__(self):
        return len(self.target)


class UEADataset(data.Dataset):
    def __init__(self, dataset, target):
        self.dataset = dataset.permute(0, 2, 1)  # (num_size, num_dimensions, series_length)
        self.target = target

    def __getitem__(self, index):
        return self.dataset[index], self.target[index]

    def __len__(self):
        return len(self.target)



if __name__ == '__main__':
    pass
