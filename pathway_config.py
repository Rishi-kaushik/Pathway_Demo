from pathway.client import Client

# Centralize Pathway client configuration
def get_client():
    return Client(
        host="localhost",      # Pathway core hostname
        port=7000,               # Pathway core port
        api_key="YOUR_API_KEY"  # If authentication enabled
    )