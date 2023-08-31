import pandas
import dotenv
import orthogonal

dotenv.load_dotenv()

client = orthogonal.Client()

y = pandas.read_csv("y_2.csv")
dataframe = client.orthogonalize(y)

print(dataframe)
