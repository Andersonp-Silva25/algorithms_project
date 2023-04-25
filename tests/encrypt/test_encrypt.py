from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 25)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("HakunaMatata", "Xablau")

    assert encrypt_message("HakunaMatata", 2) == 'atataManuk_aH'
    assert encrypt_message("Tauriell", 8) == 'lleiruaT'
