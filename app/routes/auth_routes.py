from fastapi import APIRouter, HTTPException, Body

from app.controllers.auth_controller import AuthController

router = APIRouter(prefix='/api/auth', tags=['auth'])
controller = AuthController()


@router.post('/login')
def login(dados: dict = Body(...)):
    nome = dados.get('nome')
    senha = dados.get('senha')

    usuario = controller.login(nome, senha)

    if usuario is None:
        raise HTTPException(401, 'nome ou senha inválidos')

    return usuario