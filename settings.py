from dotenv import load_dotenv
import os

# load .env file
load_dotenv()

# access a token
TOKEN = os.getenv('TOKEN')

