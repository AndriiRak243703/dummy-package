# Dummy Package - Smart Predict

A simple Python package that predicts the next number in a sequence using linear regression. Built for learning purposes - exploring packaging, CLI tools, Docker, and publishing.

## Usage

### As a Python library

```python
from dummy_package import predict_next

result = predict_next([10, 20, 30, 40])
print(result)  # 50.0
```

### As a CLI tool

```bash
smart-predict "10,20,30,40"
```

Output:

```
Next predicted value: 50.0
```