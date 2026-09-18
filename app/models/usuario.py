from app.data.usuarios_mock import USUARIOS


class Usuario:
    def __init__(self, id, nome, senha):
        self._id = id
        self.alterar_nome(nome)
        self._senha = senha

    def mostrar_id(self):
        return self._id

    def mostrar_nome(self):
        return self._nome

    def mostrar_tipo(self):
        return 'usuario'

    def alterar_nome(self, novo_nome):
        if novo_nome.strip() == '':
            raise ValueError('nome não pode ser vazio')
        self._nome = novo_nome.strip()

    def confirmar_senha(self, senha):
        return self._senha == senha

    def pode_consultar_ofertas(self):
        return True

    def pode_cadastrar_oferta(self):
        return False

    def pode_moderar_oferta(self):
        return False

    def permissoes(self):
        return {
            'consultar_ofertas': self.pode_consultar_ofertas(),
            'cadastrar_oferta': self.pode_cadastrar_oferta(),
            'moderar_oferta': self.pode_moderar_oferta(),
        }

    def __repr__(self):
        return f'{self.__class__.__name__}({self._nome})'


class Visitante(Usuario):
    def mostrar_tipo(self):
        return 'visitante'


class Contribuidor(Usuario):
    def mostrar_tipo(self):
        return 'contribuidor'

    def pode_cadastrar_oferta(self):
        return True


class Moderador(Contribuidor):
    def mostrar_tipo(self):
        return 'moderador'

    def pode_moderar_oferta(self):
        return True


PERFIS = {
    'visitante': Visitante,
    'contribuidor': Contribuidor,
    'moderador': Moderador,
}


def carregar_usuarios():
    return [PERFIS[u['perfil']](u['id'], u['nome'], u['senha'])
            for u in USUARIOS]


def autenticar(nome, senha):
    for usuario in carregar_usuarios():
        if usuario.mostrar_nome() == nome and usuario.confirmar_senha(senha):
            return usuario
    return None
