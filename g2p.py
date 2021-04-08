"""Portuguese g2p rules."""

import pynini

from pynini.lib import pynutil
from pynini.lib import rewrite


SIGMA_STAR = (
    pynini.union(
        # Non-accented graphemes.
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "ç",
        # Phonemes which aren't also graphemes.
        "ʃ",
        "ʒ",
        "ʎ",
        "ɲ",
    )
    .closure()
    .optimize()
)

_vowel = pynini.union("a", "e", "i", "o", "u")
G2P = (
    pynini.cdrewrite(pynini.cross("ch", "ʃ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("lh", "ʎ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("nh", "ɲ"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynutil.delete("h"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(
        pynini.cross("e", "i"),
        "",
        pynini.accep("s").ques + "[EOS]",
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("o", "u"),
        "",
        pynini.accep("s").ques + "[EOS]",
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(
        pynini.cross("c", "s"), "", pynini.union("i", "e"), SIGMA_STAR
    )
    @ pynini.cdrewrite(pynini.cross("c", "k"), "", "", SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("s", "z"), _vowel, _vowel, SIGMA_STAR)
    @ pynini.cdrewrite(pynini.cross("z", "s"), "", "[EOS]", SIGMA_STAR)
    @ pynini.cdrewrite(
        pynini.cross(pynini.union("ç", "ss"), "s"), "", "", SIGMA_STAR
    )
).optimize()


def g2p(istring: str) -> str:
    """Applies the G2P rule.

    Args:
      istring: the graphemic input string.

    Returns:
      The phonemic output string.

    Raises.
      rewrite.Error: composition failure.
    """
    return rewrite.one_top_rewrite(istring, G2P)
