# Solvian Machine Learning

Machine Learning infrastructure for Solvian services.

## Installing

Consider either using docker or a virtualenv to separate your python packages
from the system's. The virtualenv option is demonstrated bellow: 

```shell
virtualenv ~/envs/sml/ --python /usr/bin/python3
source ~/envs/sml/bin/activate
python setup.py install  # or develop
```

## Usage Example

### Parsers

A few parsers are implemented to convert json and csv files into
a pandas DataFrame, ideal to feed machine learning models with:

```python
from solvian.ml.infrastructure.parsers import JsonParser

parser = JsonParser(content='path/to/file.json',
                    ignore_features=['temperature'])
# or `parser = CsvParser(content='path/to/file.csv', ...)`

d = parser.process()

print('features:', d.columns)
print(d.head())

m = SomeMachineLearningModel(...)
print(m.predict(d))
```
