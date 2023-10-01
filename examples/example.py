import pandas
import dotenv
import orthogonal
import datetime

dotenv.load_dotenv()

client = orthogonal.Client()

y = pandas.read_csv("y.csv")
print(y.head())

def now(message: str):
    print(datetime.datetime.now(), message)

now("orthogonalize: no jacobians: start")
dataframe = client.orthogonalize(
    y,
    date_column_name="Moons",
    alpha=0.346,
)
now("orthogonalize: no jacobians: end")
print(dataframe.head())

now("orthogonalize: witn jacobians: start")
dataframe, jacobians = client.orthogonalize(
    y,
    date_column_name="Moons",
    alpha=0.346,
    compute_jacobians=True,
)
now("orthogonalize: no jacobians: end")
print(dataframe.head())
print(str(jacobians)[:100])

# import pdb; pdb.set_trace()
