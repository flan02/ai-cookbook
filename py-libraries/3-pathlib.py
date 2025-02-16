import pandas as pd
from pathlib import Path

file_path = Path(__file__).parent / "data" / "test.csv" # ? This library is used to create a path object

df = pd.read_csv(file_path)
# df = pd.read_csv(file_path.resolve()) # ? Absolute path

print(df)

print(Path().cwd()) # ? Current working directory
print(Path().home()) # ? Home directory
print(Path().home() / "Code") # ? Home directory + custom directory
