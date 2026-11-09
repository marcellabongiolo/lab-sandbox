import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch
import getpass

from senha_segura import analisar_forca_senha, main


class TestAnalisarForcaSenha(unittest.TestCase):
    def test_senha_forte(self):
        resultado = analisar_forca_senha("SenhaSegura9!")
        self.assertEqual(resultado["pontos"], 5)
        self.assertEqual(resultado["classificacao"], "forte")

    def test_senha_media(self):
        resultado = analisar_forca_senha("Senha123")
        self.assertEqual(resultado["pontos"], 4)
        self.assertEqual(resultado["classificacao"], "media")

    def test_senha_fraca(self):
        resultado = analisar_forca_senha("abc")
        self.assertEqual(resultado["pontos"], 1)
        self.assertEqual(resultado["classificacao"], "fraca")

    def test_criterios_individuais(self):
        criterios = analisar_forca_senha("abc12345")["criterios"]
        self.assertTrue(criterios["tamanho_minimo"])
        self.assertFalse(criterios["maiuscula"])
        self.assertTrue(criterios["minuscula"])
        self.assertTrue(criterios["numero"])
        self.assertFalse(criterios["especial"])

    def test_string_vazia(self):
        resultado = analisar_forca_senha("")
        self.assertEqual(resultado["tamanho"], 0)
        self.assertEqual(resultado["classificacao"], "fraca")

    def test_tipo_invalido(self):
        with self.assertRaises(TypeError):
            analisar_forca_senha(12345678)


class TestEntradaPrivada(unittest.TestCase):
    def test_cli_usa_entrada_oculta_sem_revelar_senha(self):
        saida = io.StringIO()
        with patch("senha_segura.getpass.getpass", return_value="SenhaSegura9!") as entrada:
            with redirect_stdout(saida):
                main()
        entrada.assert_called_once()
        self.assertNotIn("SenhaSegura9!", saida.getvalue())
        self.assertIn("forte", saida.getvalue())

    def test_interrompe_quando_terminal_nao_permite_entrada_oculta(self):
        saida = io.StringIO()
        with patch("senha_segura.getpass.getpass", side_effect=getpass.GetPassWarning):
            with redirect_stdout(saida):
                main()
        self.assertIn("Entrada oculta indisponível", saida.getvalue())
        self.assertNotIn("Classificação heurística", saida.getvalue())


if __name__ == "__main__":
    unittest.main()
