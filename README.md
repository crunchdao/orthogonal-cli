# Orthogonal CLI

Here is the Orthogonal CLI for the DataCrunch competition by [CrunchDAO](https://www.crunchdao.com/).

## Installation

Use [pip](https://pypi.org/project/orthogonal-cli/) to install the `orthogonal-cli`.

```bash
pip install orthogonal-cli --upgrade
```

## Usage

This library require a [CrunchDAO's API Key](https://account.crunchdao.com/account/api).

```python
import orthogonal

client = orthogonal.Client(
    api_key="..." # can also be read from CRUNCHDAO_API_KEY environment variable.
)

y = pandas.read_csv("y.csv", index_col=0)
print(y.head())
#          Moons       id      abcd
# 1030371      1  AAAAAAA -2.122527
# 1030372      1  BBBBBBB -0.386952
# 1030373      1  CCCCCCC  0.028175
# 1030374      1  DDDDDDD -1.276682
# 1030375      1  EEEEEEE  0.939289

dataframe, jacobians = client.orthogonalize(y)
dataframe = client.orthogonalize(y, compute_jacobians=False) # or ignore jacobians
print(dataframe.head())
#    Moons       id      abcd
# 0      1  AAAAAAA -2.149988
# 1      1  BBBBBBB -0.395232
# 2      1  CCCCCCC  0.030502
# 3      1  DDDDDDD -1.311531
# 4      1  EEEEEEE  0.917134
```

Please see [here](https://github.com/crunchdao/orthogonal/blob/master/api/service/orthogonalize.py) for the backend implementation.

## Contributing

Pull requests are always welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue in the GitHub repository.

## License

[MIT](https://choosealicense.com/licenses/mit/)
