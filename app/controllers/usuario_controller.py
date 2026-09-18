from app.models.usuario import autenticar


class UsuarioController:
    def login(self, nome, senha):
        usuario = autenticar(nome, senha)
        if usuario is None:
            return None
        return self._para_dicionario(usuario)

    def _para_dicionario(self, usuario):
        return {
            'id': usuario.mostrar_id(),
            'nome': usuario.mostrar_nome(),
            'perfil': usuario.mostrar_tipo(),
            'permissoes': usuario.permissoes(),
        }
