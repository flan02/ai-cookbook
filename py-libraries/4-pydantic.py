from textwrap import indent
from pydantic import BaseModel, field_validator, SecretStr, Field, EmailStr
from rich import traceback

traceback.install()

class Account(BaseModel):
  name: str = Field(..., min_length=3, max_length=50)
  password: SecretStr
  balance: float = 2.0

  @field_validator("balance")
  def balance_must_be_positive(cls, value):
    if value < 0:
      raise ValueError("balance must be positive")
    else:
      return value

if __name__ == "__main__":

  password = SecretStr("Axk01") # ? SecretStr is a wrapper around str that ensures that the value is always a str and that it is not exposed in tracebacks.
  account = Account(name="John Doe", password=password, balance=100.0)
  print(account.name)
  print(account.balance)
  print(account.model_dump())