"""Unit tests for Portuguese G2P."""

import unittest

import g2p


class G2PTest(unittest.TestCase):
    def rewrites(self, istring: str, expected_ostring: str) -> None:
        """Asserts that the g2p rule produces the correct output.

        Note that this itself is not a unit test because its name does not
        begin with `test_`; but it can be used to implement other unit tests.

        Args:
            istring: the input string
            expected_ostring: the expected output string.
        """
        ostring = g2p.g2p(istring)
        self.assertEqual(ostring, expected_ostring)

    def test_cases(self):
        self.rewrites("cases", "kazis")

    def test_cimento(self):
        self.rewrites("cimento", "simentu")

    def test_chato(self):
        self.rewrites("chato", "ʃatu")

    def test_casa(self):
        self.rewrites("casa", "kaza")

    def test_filho(self):
        self.rewrites("filho", "fiʎu")

    def test_homem(self):
        self.rewrites("homem", "omem")

    def test_ninho(self):
        self.rewrites("ninho", "niɲu")

    def test_vez(self):
        self.rewrites("vez", "ves")


if __name__ == "__main__":
    unittest.main()
