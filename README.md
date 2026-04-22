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

### As an API

Start the server:

```bash
poetry run uvicorn dummy_package.api:app --reload
```

The API will be available at `http://localhost:8000`. You can explore and test all endpoints interactively at `http://localhost:8000/docs`.

Available endpoints:

- `GET /` - Returns a welcome message
- `GET /hello/{name}` - Returns a personalized greeting
- `GET /predict?numbers=1,2,3,4` - Predicts the next number in a comma-separated sequence

Example using Python:

```python
import requests

response = requests.get("http://localhost:8000/predict?numbers=10,20,30,40")
print(response.json())  # {"Next predicted value": 50.0}
```

Or just open the URL directly in your browser:

```
http://localhost:8000/predict?numbers=10,20,30,40
```