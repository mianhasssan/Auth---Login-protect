from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Read configuration values
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
PORT = int(os.getenv("PORT", 8000))