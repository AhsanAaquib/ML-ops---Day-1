import torch

import torch.nn as nn
import torch.nn.functional as F

class DummyConvNet(nn.Module):
    def __init__(self, num_classes=10):
        super(DummyConvNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(32 * 8 * 8, 128)
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))  # [batch, 16, 16, 16]
        x = self.pool(F.relu(self.conv2(x)))  # [batch, 32, 8, 8]
        x = x.view(x.size(0), -1)             # Flatten
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Example usage:
# model = DummyConvNet(num_classes=10)
# print(model)