from dotenv import load_dotenv
import os

IS_REPL = True

# load .env file

if IS_REPL:
  TOKEN = os.environ['TOKEN']
else:
  load_dotenv()
  TOKEN = os.getenv('TOKEN')
