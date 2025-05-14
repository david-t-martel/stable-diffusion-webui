# save as test_oneapi.py
import os

import numpy as np
import torch

print(f"OneAPI Root: {os.environ.get('ONEAPI_ROOT', 'Not found')}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA device count: {torch.cuda.device_count()}")
if torch.cuda.is_available():
    print(f"CUDA device name: {torch.cuda.get_device_name(0)}")

# Test Intel MKL if available
try:
    import intel_extension_for_pytorch as ipex

    print("Intel Extension for PyTorch is available")

    # Create a simple tensor operation that might use MKL
    a = torch.randn(1000, 1000)
    b = torch.randn(1000, 1000)
    c = torch.matmul(a, b)
    print("Matrix multiplication completed")
except ImportError:
    print("Intel Extension for PyTorch is not installed")
