import torch
X = torch.randn(3, 4)
print(X.shape)
Y = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0 ,8.0, 9.0], [10.0, 11.0, 12.0]])
print(X @ Y)
Z = torch.arange(4.0, requires_grad=True)
f = 3 * torch.dot(Z, Z)
f.backward()
print(Z.grad)
