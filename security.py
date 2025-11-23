from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class SecurityService:
    @staticmethod
    def gerar_hash(senha: str) -> str:
        return pwd_context.hash(senha)

    @staticmethod
    def verificar_senha(senha_pura: str, senha_hash: str) -> bool:
        return pwd_context.verify(senha_pura, senha_hash)