from fastapi.security import APIKeyHeader
from fastapi import HTTPException, status, Security

# API Keys - this would in a real app be stored elsewhere, not hardcoded (example only)
api_keys = ['abc123']
security_scheme = APIKeyHeader(name="x-api-key")

def auth_api_key(input_api_key_string: str = Security(security_scheme)):
    if input_api_key_string not in api_keys:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            'Invalid api key'
        )