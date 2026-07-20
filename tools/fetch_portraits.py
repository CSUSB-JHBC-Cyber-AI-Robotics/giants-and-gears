"""Pull mathematician portraits out of the offline Wikipedia image index.

Search is CLIP (ultra img index `wikipedia_images`); the pick is the highest
hit whose caption contains every required word (usually the surname), so a
lookalike engraving of someone else never wins. Bytes come straight from the
ZIM via libzim — no Kiwix server needed.

Run with the interpreter that has numpy/torch/PIL:  py -3.11 fetch_portraits.py
"""
import io
import re
import sys
import urllib.parse
from pathlib import Path

ULTRA = Path(r"C:\Users\desmo\AI Programs\Ultra-PC")
sys.path.insert(0, str(ULTRA))

from ultrapc import imgsearch, zimimg  # noqa: E402
from libzim.reader import Archive      # noqa: E402
from PIL import Image                   # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "assets" / "img" / "portraits"
OUT.mkdir(parents=True, exist_ok=True)

_archives: dict[str, Archive] = {}


def _archive(book: str) -> Archive:
    if book not in _archives:
        z = zimimg.resolve_zim(book)
        if z is None:
            raise FileNotFoundError(f"no local ZIM matches '{book}'")
        _archives[book] = Archive(str(z))
    return _archives[book]


def fetch(query: str, must_contain: list[str], out_name: str, k: int = 16) -> bool:
    dest = OUT / f"{out_name}.jpg"
    if dest.exists():
        print(f"  -- {out_name}: already fetched")
        return True
    hits = imgsearch.search("wikipedia_images", query, k)
    pick = None
    for h in hits:
        title = h["file"].lower()
        if all(w.lower() in title for w in must_contain):
            pick = h
            break
    if pick is None:
        print(f"  !! {out_name}: nothing matched {must_contain}; top hits were:")
        for h in hits[:6]:
            print(f"       {h['score']:.3f}  {h['file']}")
        return False
    m = re.match(r"https?://[^/]+/content/([^/]+)/(.+)$", pick["abs"])
    if not m:
        print(f"  !! {out_name}: unparseable target {pick['abs']}")
        return False
    book, path = m.group(1), urllib.parse.unquote(m.group(2))
    data = bytes(_archive(book).get_entry_by_path(path).get_item().content)
    img = Image.open(io.BytesIO(data))
    img.load()
    img = img.convert("RGB")
    if max(img.size) > 900:
        img.thumbnail((900, 900))
    img.save(dest, "JPEG", quality=88)
    print(f"  ok {out_name}: {pick['file']}  ({img.size[0]}x{img.size[1]})")
    return True


# (query, caption-must-contain, output name)
WANTED = [
    ("marble bust of Pythagoras ancient greek", ["pythagoras"], "pythagoras"),
    ("painting of Euclid ancient greek mathematician", ["euclid"], "euclid"),
    ("painting of Archimedes", ["archimedes"], "archimedes"),
    ("engraving of Hipparchus greek astronomer", ["hipparchus"], "hipparchus"),
    ("medieval portrait of Ptolemy astronomer", ["ptolemy"], "ptolemy"),
    ("statue of Aryabhata indian mathematician", ["aryabhata"], "aryabhata"),
    ("statue or stamp of al-Khwarizmi persian mathematician", ["khwarizmi"], "al-khwarizmi"),
    ("portrait painting of Rene Descartes", ["descartes"], "descartes"),
    ("portrait painting of Isaac Newton", ["newton"], "newton"),
    ("portrait painting of Gottfried Wilhelm Leibniz", ["leibniz"], "leibniz"),
    ("portrait painting of Leonhard Euler", ["euler"], "euler"),
    ("portrait painting of Carl Friedrich Gauss", ["gauss"], "gauss"),
    ("portrait of Joseph-Louis Lagrange", ["lagrange"], "lagrange"),
    ("portrait of Jean-Baptiste Joseph Fourier", ["fourier"], "fourier"),
    ("portrait of William Rowan Hamilton mathematician", ["hamilton"], "hamilton"),
    ("photograph of Emmy Noether mathematician", ["noether"], "noether"),
    ("photograph of Sofia Kovalevskaya mathematician", ["kovalevskaya"], "kovalevskaya"),
    ("photograph of Alan Turing", ["turing"], "turing"),
    ("photograph of Claude Shannon engineer", ["shannon"], "shannon"),
    ("photograph of Norbert Wiener mathematician cybernetics", ["wiener"], "wiener"),
    ("photograph of Rudolf Kalman engineer", ["kalman"], "kalman"),
    ("photograph of Katherine Johnson NASA mathematician", ["johnson"], "katherine-johnson"),
]

if __name__ == "__main__":
    got = sum(fetch(q, need, name) for q, need, name in WANTED)
    print(f"\n{got}/{len(WANTED)} portraits fetched -> {OUT}")
