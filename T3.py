import torch


# 1.生成数据
X = torch.randn(1000, 1)
y = 2 * X + 3 + torch.randn(1000, 1) * 0.01

