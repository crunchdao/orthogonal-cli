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
#                date  symbol       abcd
# 1030371  2023-01-06  AAAAAAA -2.122527
# 1030372  2023-01-06  BBBBBBB -0.386952
# 1030373  2023-01-06  CCCCCCC  0.028175
# 1030374  2023-01-06  DDDDDDD -1.276682
# 1030375  2023-01-06  EEEEEEE  0.939289

dataframe = client.orthogonalize(y)
print(dataframe.head())
#          date  symbol       abcd
# 0  2023-01-06  AAAAAAA -2.149988
# 1  2023-01-06  BBBBBBB -0.395232
# 2  2023-01-06  CCCCCCC  0.030502
# 3  2023-01-06  DDDDDDD -1.311531
# 4  2023-01-06  EEEEEEE  0.917134
```

Please see [here](https://github.com/crunchdao/orthogonal/blob/master/api/service/orthogonalize.py) for the backend implementation.

## Contributing

Pull requests are always welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue in the GitHub repository.

## License

[MIT](https://choosealicense.com/licenses/mit/)
