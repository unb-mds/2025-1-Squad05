from src.backend.database.database import users_db
from src.backend.models.modelos import UsuarioRegistro, UsuarioLogin
from src.backend.utils.utilities import hash_password, verify_password, generate_token

def register_user(user: UsuarioRegistro) -> bool:
    if user.email in users_db:
        return False
    hashed_password = hash_password(user.password)
    users_db[user.email] = {"password": hashed_password}
    return True

def login_user(user: UsuarioLogin) -> str:
    user_data = users_db.get(user.email)
    if not user_data or not verify_password(user.password, user_data["password"]):
        return None
    return generate_token(user.email)
