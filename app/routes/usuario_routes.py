from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.controllers.usuario_controller import UsuarioController

router = APIRouter(prefix='/api/login', tags=['login'])
controller = UsuarioController()


class LoginEntrada(BaseModel):
    nome: str
    senha: str


@router.post('')
def login(dados: LoginEntrada):
    usuario = controller.login(dados.nome, dados.senha)
    if usuario is None:
        raise HTTPException(401, 'nome ou senha inválidos')
    return usuario
