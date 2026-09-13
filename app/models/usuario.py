from app.data.usuarios_mock import USUARIOS 

#criei a classe principal com as informações de usuário e classes heranças, para atribuir os tres tipos de usuários
class Usuario:
    def __init__(self, id, nome, senha):
        self._id = id
        self._nome = nome
        self._senha = senha

    def mostrar_id(self):
        return self._id

    def mostrar_nome(self):
        return self._nome

    def mostrar_perfil(self):
        return type(self).__name__
    
    def conferir_senha(self,senha):
        return self._senha == senha

    def pode_favoritar(self):
        return True
        
    def pode_publicar(self):
        return False
        
    def pode_moderar(self):
        return False

class Visitante(Usuario):
      #Classe herança, do perfil visitante. Não atribuo nenhum parametro ou função, porque a classe principal 
      #já atende o perfil de visitante, utilizo pass para repassar os atributos e métdodos da classe. 
    pass

#Classe herança, do perfil contribuidor, retorno true ao atributo pode_publicar.
class Contribuidor(Usuario):
    def pode_publicar(self):
        return True

#Classe herança, do perfil moderador, retorno true ao atributo pode_moderar.
class Moderador(Contribuidor):
    def pode_moderar(self):
        return True

PERFIS = {
'visitante': Visitante,
'contribuidor': Contribuidor,
'moderador': Moderador,
}

def carregar_usuarios():
    return [PERFIS[u['perfil']](u['id'], u['nome'], u['senha'])
            for u in USUARIOS]

# def autenticar(nome, senha):
#     for usuario in carregar_usuarios():
#         if usuario.mostrar_nome() == nome and usuario.conferir_senha(senha):
#             return usuario
#     return None

