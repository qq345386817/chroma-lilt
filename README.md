# ChromaLilt web

Static marketing, help, support, and privacy pages for ChromaLilt.

Production domain: `https://chroma-lilt.luopeike.com`

## Build

```sh
python3 scripts/build_site.py
```

The generator writes localized pages under:

- `en-US/`
- `zh-Hans/`
- `zh-Hant/`
- `ja/`
- `ko/`
- `de-DE/`
- `fr-FR/`
- `es-ES/`

Root pages redirect to the English version while localized pages carry canonical and `hreflang` metadata for search engines.
