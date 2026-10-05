from supabase import create_client, Client
from config.settings import SUPABASE_URL, SUPABASE_KEY

def get_supabase_client() -> Client:
    """Cria e retorna uma instância do cliente Supabase."""
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase: Client = get_supabase_client()