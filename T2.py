import torch
X = torch.randn(3, 4)
print(X.shape)
Y = torch.tensor([[1, 2, 3, 4], [5, 6, 7 ,8], [1, 2, 3, 4]])
print(X * Y)
Z = torch.arange(4.0, requires_grad=True)
f = 3 * torch.dot(Z, Z)
f.backward()
print(Z.grad)
