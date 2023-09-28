import pandas
import dotenv
import orthogonal

dotenv.load_dotenv()

client = orthogonal.Client()

y = pandas.read_csv("y.csv", index_col=0)
print(y.head())

dataframe = client.orthogonalize(
    y,
    date_column_name="date",
    risk_exposures=[0.45, 0.86, 0.20, 0.42],
)
print(dataframe.head())
