import pandas
import dotenv
import orthogonal

dotenv.load_dotenv()

client = orthogonal.Client()

y = pandas.read_csv("y.csv")
print(y.head())

dataframe, jacobians = client.orthogonalize(
    y,
    date_column_name="Moons",
    alpha=0.346,
)
print(dataframe.head())
print(str(jacobians)[:100])

# import pdb; pdb.set_trace()
