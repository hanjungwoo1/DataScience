import torch
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.get_device_name(torch.cuda.current_device()))

# True
# 1
# NVIDIA GeForce RTX 3070 Ti