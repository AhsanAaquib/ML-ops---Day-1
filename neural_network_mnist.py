import torch

import torch.nn as nn
import torch.nn.functional as F

class DummyNeuralNet(nn.Module):
    def __init__(self, input_size=784, hidden_size=128, num_classes=10):
        super(DummyNeuralNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Example usage with random data
if __name__ == "__main__":
    # Simulate a batch of 16 images, each flattened to 784 features (28x28)
    sample_data = torch.randn(16, 784)
    model = DummyNeuralNet()
    output = model(sample_data)
    print("Output shape:", output.shape)  # Should be [16, 10]