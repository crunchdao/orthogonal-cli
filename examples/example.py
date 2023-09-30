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
    alpha=0.346,
)
print(dataframe.head())
