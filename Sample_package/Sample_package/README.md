# Sample_package

`Sample_package` is a Python package for making predictions using a trained machine learning model. It includes modules for data preprocessing, prediction pipelines, and model management.

## Installation

```bash
pip install Sample_package

```
## Exception

### Paths in `config.py` Not Integrated

The `config.py` file has been added to the project to manage paths for datasets, trained models, and other resources. However, **these paths have not yet been integrated into the Python code**. Currently, the code uses hardcoded paths for accessing datasets and trained models. 

To make the code more flexible and portable across different environments, the paths in `config.py` should be used instead of hardcoding them.

For example, instead of hardcoding paths for datasets or trained models, you should use the paths from `config.py` like this:


```bash
from Sample_package.prediction_model.config import config
```


# Access paths from the config
model_path = config.MODEL_PATH
dataset_path = config.DATASET_PATH