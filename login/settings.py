from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.load_config import LoadConfig

class CsrfSettings(LoadConfig):
    secret_key: str = "testtoken"
    cookie_samesite: str = "none"
    cookie_secure: bool = True
    # token_location: str = "body"
    # token_key: str = "client_secret"

class LoginCsrfSettings(CsrfSettings):
    max_age: int = 30
    
class AccessCsrfSettings(CsrfSettings):
    max_age: int = 300
    
    
class LoginCSRF(CsrfProtect):
    ...
    
class AccessCSRF(CsrfProtect):
    ...

LoginCSRF.load_config(lambda: LoginCsrfSettings())
AccessCSRF.load_config(lambda: AccessCsrfSettings())