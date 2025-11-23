from typing import List, Optional
from schemas import UsuarioCreate, UsuarioPublic
from security import SecurityService

class UsuarioRepository:
    def __init__(self):
        self.db = []
        self.id_counter = 1

    def criar(self, usuario: UsuarioCreate) -> UsuarioPublic:
        if self.buscar_por_username(usuario.username):
            return None

        novo_usuario = {
            "id": self.id_counter,
            "username": usuario.username,
            "email": usuario.email,
            "senha_hash": SecurityService.gerar_hash(usuario.senha) # Criptografa antes de salvar
        }
        
        self.db.append(novo_usuario)
        self.id_counter += 1
        
        return UsuarioPublic(**novo_usuario)

    def buscar_por_username(self, username: str) -> Optional[dict]:
        for u in self.db:
            if u["username"] == username:
                return u
        return None

    def listar_todos(self) -> List[UsuarioPublic]:
        return [UsuarioPublic(**u) for u in self.db]

db_instance = UsuarioRepository()