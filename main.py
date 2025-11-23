from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware 
from typing import List, Annotated
from schemas import SorteioRequest, SorteioResponse, UsuarioCreate, UsuarioLogin, UsuarioPublic
from logic import SorteadorService
from repository import db_instance, UsuarioRepository
from security import SecurityService

app = FastAPI(
    title="Amigo Secreto dos Pedradas",
    version="1.0.0",
    summary="Sistema de Sorteio dos Pedradas"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

def get_repo() -> UsuarioRepository:
    return db_instance

def get_sorteador() -> SorteadorService:
    return SorteadorService()

@app.post("/auth/cadastro", response_model=UsuarioPublic, status_code=status.HTTP_201_CREATED, tags=["Usuários"])
async def registrar_usuario(
    usuario: UsuarioCreate,
    repo: Annotated[UsuarioRepository, Depends(get_repo)]
):
    novo_user = repo.criar(usuario)
    if not novo_user:
        raise HTTPException(status_code=400, detail="Username já existe.")
    return novo_user

@app.post("/auth/login", tags=["Usuários"])
async def login(
    dados: UsuarioLogin,
    repo: Annotated[UsuarioRepository, Depends(get_repo)]
):
    user_db = repo.buscar_por_username(dados.username)
    
    if not user_db or not SecurityService.verificar_senha(dados.senha, user_db['senha_hash']):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    
    return {
        "mensagem": f"Bem-vindo de volta, {user_db['username']}! Login realizado.",
        "usuario": {
            "id": user_db["id"],
            "username": user_db["username"],
            "email": user_db["email"]
        }
    }

@app.get("/usuarios", response_model=List[UsuarioPublic], tags=["Usuários"])
async def listar_usuarios(repo: Annotated[UsuarioRepository, Depends(get_repo)]):
    return repo.listar_todos()

@app.post("/sorteio", response_model=SorteioResponse, tags=["Sorteio"])
async def criar_sorteio(
    dados: SorteioRequest, 
    service: Annotated[SorteadorService, Depends(get_sorteador)]
):
    resultado = service.realizar_sorteio(dados.nomes)
    return SorteioResponse(total_participantes=len(dados.nomes), pares=resultado)