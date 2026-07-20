"""Fallback portrait fetcher: read a person's Wikipedia ARTICLE from the text
ZIM and extract its lead (infobox) image — deterministic, unlike CLIP captions.

Run:  py -3.11 fetch_from_article.py
"""
import io
import re
import sys
import urllib.parse
from pathlib import Path

ULTRA = Path(r"C:\Users\desmo\AI Programs\Ultra-PC")
sys.path.insert(0, str(ULTRA))

from ultrapc import zimimg            # noqa: E402
from libzim.reader import Archive      # noqa: E402
from PIL import Image                   # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "assets" / "img" / "portraits"
ZIM = zimimg.resolve_zim("wikipedia_en_all_maxi_2026-02")
arch = Archive(str(ZIM))


def entry(path: str):
    for p in (path, f"A/{path}"):
        try:
            e = arch.get_entry_by_path(p)
            while e.is_redirect:
                e = e.get_redirect_entry()
            return e
        except KeyError:
            continue
    return None


def fetch(article: str, out_name: str) -> bool:
    dest = OUT / f"{out_name}.jpg"
    if dest.exists():
        print(f"  -- {out_name}: already fetched")
        return True
    e = entry(article)
    if e is None:
        print(f"  !! {out_name}: article '{article}' not found")
        return False
    html = bytes(e.get_item().content).decode("utf-8", "replace")
    # first content image in the page = the infobox/lead portrait
    srcs = re.findall(r'<img[^>]+src="([^"]+)"', html)
    art_dir = e.path.rsplit("/", 1)[0] if "/" in e.path else ""
    for src in srcs:
        raw = urllib.parse.unquote(src)
        # resolve relative to the article's own path
        parts = (art_dir.split("/") if art_dir else [])
        for seg in raw.split("/"):
            if seg == "..":
                parts = parts[:-1]
            elif seg in (".", ""):
                continue
            else:
                parts.append(seg)
        img_path = "/".join(parts)
        try:
            it = arch.get_entry_by_path(img_path).get_item()
        except KeyError:
            continue
        if not it.mimetype.startswith("image/") or it.mimetype.endswith("svg+xml"):
            continue
        data = bytes(it.content)
        try:
            img = Image.open(io.BytesIO(data))
            img.load()
        except Exception:
            continue
        if min(img.size) < 120:      # skip icons/thumbnails
            continue
        img = img.convert("RGB")
        if max(img.size) > 900:
            img.thumbnail((900, 900))
        img.save(dest, "JPEG", quality=88)
        print(f"  ok {out_name}: {img_path}  ({img.size[0]}x{img.size[1]})")
        return True
    print(f"  !! {out_name}: no usable image among {len(srcs)} img tags")
    return False


WANTED = [
    ("Euclid", "euclid"),
    ("Archimedes", "archimedes"),
    ("Hipparchus", "hipparchus"),
    ("Muhammad_ibn_Musa_al-Khwarizmi", "al-khwarizmi"),
    ("Joseph-Louis_Lagrange", "lagrange"),
    ("Joseph_Fourier", "fourier"),
    ("Rudolf_E._Kalman", "kalman"),
]

if __name__ == "__main__":
    got = sum(fetch(a, n) for a, n in WANTED)
    print(f"\n{got}/{len(WANTED)} fetched -> {OUT}")
