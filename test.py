import torch

print(f"Pytorch 版本：{torch.__version__}")

if torch.backends.mps.is_available():
    print("成功了！")
else:
    print("MPS 不可用，出问题了！")
