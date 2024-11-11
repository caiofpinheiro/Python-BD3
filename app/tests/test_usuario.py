import pytest

from app.models.usuario_model import Usuario

@pytest.fixture

def test_usuario_nome_vazio():
    with pytest.raises(ValueError, match= "nome vazio."):
        Usuario("", "caio@gmail.com","1234")

def test_usuario_nome_invalido():
    with pytest.raises(TypeError, match = "nome invalido."):
        Usuario(112,"caio@gmail.com","1234")

def test_usuario_email_vazio():
    with pytest.raises(ValueError, match= "email vazio."):
        Usuario("caio", "", "1234")

def test_usuario_email_invalido():
    with pytest.raises(TypeError, match = "email invalido."):
        Usuario("caio", 123, "1234")

def test_usuario_senha_vazia():
    with pytest.raises(ValueError, match= "senha vazia."):
        Usuario("caio", "caio@gmail.com", "")

def test_usuario_senha_invalida():
    with pytest.raises(TypeError, match = "senha invalida."):
        Usuario("caio","caio@gmail.com", 1234)