import pandas
import dotenv
import orthogonal

dotenv.load_dotenv()

client = orthogonal.Client()

y = pandas.read_csv("y.csv", index_col=0)
print(y.head())

dataframe = client.orthogonalize(y)
print(dataframe.head())
