"""Fetch a SPECIFIC image from a Wikipedia article by filename substring
(fetch_from_article takes the first usable image; this one lets you aim).

Usage:  py -3.11 fetch_named_image.py <article> <src-substring> <out-name>
"""
import io
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_from_article import arch, entry, OUT  # noqa: E402
from PIL import Image                             # noqa: E402


def fetch_named(article: str, frag: str, out_name: str) -> bool:
    e = entry(article)
    if e is None:
        print(f"  !! article '{article}' not found")
        return False
    html = bytes(e.get_item().content).decode("utf-8", "replace")
    srcs = re.findall(r'<img[^>]+src="([^"]+)"', html)
    art_dir = e.path.rsplit("/", 1)[0] if "/" in e.path else ""
    frag_l = frag.lower()
    for src in srcs:
        raw = urllib.parse.unquote(src)
        if frag_l not in raw.lower():
            continue
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
        if not it.mimetype.startswith("image/"):
            continue
        img = Image.open(io.BytesIO(bytes(it.content)))
        img.load()
        img = img.convert("RGB")
        if max(img.size) > 900:
            img.thumbnail((900, 900))
        dest = OUT / f"{out_name}.jpg"
        img.save(dest, "JPEG", quality=88)
        print(f"  ok {out_name}: {img_path}  ({img.size[0]}x{img.size[1]})")
        return True
    print(f"  !! no image matching '{frag}' in {article}; candidates:")
    for s in srcs[:10]:
        print("     ", urllib.parse.unquote(s).rsplit("/", 1)[-1])
    return False


if __name__ == "__main__":
    fetch_named(sys.argv[1], sys.argv[2], sys.argv[3])
