import torch

# Define a tensor with gradient tracking enabled
x = torch.tensor(2., requires_grad=True)

# Define a function y within the torch.no_grad context
with torch.no_grad():
    y = x ** 2

# Check if gradient is required for y
print("y.requires_grad:", y.requires_grad)  # Output: False
