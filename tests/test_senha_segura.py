import unittest

from senha_segura import analisar_forca_senha


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
        self.assertEqual(resultado["pontos"], 2)
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


if __name__ == "__main__":
    unittest.main()
