import os

# Establecer manualmente la clave de API
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

# Ahora puedes obtener la API key
api_key = os.getenv("OPENAI_API_KEY")
print(api_key)
if api_key:
    print(api_key)  # Para verificar si se cargó correctamente
else:
    print("Can not load OPENAI_API_KEY")
# ? To run this script in jupyter notebook
# $ %run 1-basic.py





# from dotenv import load_dotenv
# import os

# # Ruta absoluta o relativa al archivo .env
# from pathlib import Path

# dotenv_path = Path("./env")  # Ajusta según la ubicación real
# load_dotenv(dotenv_path=dotenv_path)

# # Ahora puedes obtener la API key
# api_key = os.getenv("OPENAI_API_KEY")
# if api_key:
#     print(api_key)  # Para verificar si se cargó correctamente
# else:
#     print("Can not load OPENAI_API_KEY")


