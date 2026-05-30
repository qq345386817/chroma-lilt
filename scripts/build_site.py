#!/usr/bin/env python3
from __future__ import annotations

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://chroma-lilt.luopeike.com"
APP_STORE_URL = "https://apps.apple.com/search?term=ChromaLilt"

LOCALES = [
    ("en-US", "en", "English"),
    ("zh-Hans", "zh-Hans", "简体中文"),
    ("zh-Hant", "zh-Hant", "繁體中文"),
    ("ja", "ja", "日本語"),
    ("ko", "ko", "한국어"),
    ("de-DE", "de", "Deutsch"),
    ("fr-FR", "fr", "Français"),
    ("es-ES", "es", "Español"),
]

COPY = {
    "en-US": {
        "nav_home": "Home",
        "nav_help": "Help",
        "nav_support": "Support",
        "nav_privacy": "Privacy",
        "language": "Language",
        "kicker": "Calm coloring app for iPhone and iPad",
        "title": "ChromaLilt",
        "description": "ChromaLilt is a relaxing coloring app with Hold to Bloom gestures, soft smart-edge brush strokes, local progress, and a quiet Color Journal.",
        "lead": "Press inside structured line-art regions and watch pigment unfold. Switch to the clipped brush for gentle strokes, finish your page, and keep a small color journal of calm moments.",
        "download": "Download on the App Store",
        "preview_label": "ChromaLilt coloring preview",
        "stat_one": "Hold to Bloom",
        "stat_two": "Smart Edge Brush",
        "stat_three": "Color Journal",
        "section_features": "Designed for short, mindful coloring sessions",
        "feature_1_title": "Bloom with pressure",
        "feature_1": "Long-press a region to grow a soft watercolor bloom without leaving the line art.",
        "feature_2_title": "Brush inside edges",
        "feature_2": "The smart brush keeps soft strokes clipped to the active shape so pages stay tidy.",
        "feature_3_title": "Save every page",
        "feature_3": "Progress is stored locally, finished works appear in the journal, and exports can be shared as images.",
        "section_art": "Starter artwork included",
        "art_copy": "Begin with tiny worlds, flowers, cozy room details, and mindful pattern pages. Each artwork is structured for ChromaLilt's bloom and brush tools.",
        "guide_title": "Need help?",
        "guide_copy": "Learn the core gestures, export flow, and privacy model before your first coloring session.",
        "footer": "ChromaLilt - calm coloring that blooms.",
        "help_title": "ChromaLilt Help",
        "help_desc": "Learn how to use Hold to Bloom, Smart Edge Brush, Color Journal, and image export in ChromaLilt.",
        "help_intro": "ChromaLilt is built around slow, local coloring sessions. Start from the Gallery, choose a mood palette, then color with blooms or brush strokes.",
        "help_steps": [
            ("Start a page", "Open Gallery and choose Daily Bloom or any starter artwork."),
            ("Hold to Bloom", "Press and hold inside a region to grow a soft pigment bloom."),
            ("Use Brush", "Switch to Brush to draw clipped strokes inside the current artwork shape."),
            ("Finish and export", "Mark a page finished for the Color Journal, or export an image for sharing."),
        ],
        "support_title": "ChromaLilt Support",
        "support_desc": "Contact ChromaLilt support for help with coloring, export, journal, or App Store questions.",
        "support_body": "For support, feature requests, or bug reports, email us with your device model, iOS version, and a short description of what happened.",
        "privacy_title": "ChromaLilt Privacy Policy",
        "privacy_desc": "ChromaLilt stores coloring progress locally and does not require an account.",
        "privacy_body": "ChromaLilt is designed as a local, private coloring space. Coloring progress and journal state are stored on your device. The app does not require an account. If you contact support, we use the information you send only to answer your request.",
    },
    "zh-Hans": {
        "nav_home": "首页",
        "nav_help": "帮助",
        "nav_support": "支持",
        "nav_privacy": "隐私",
        "language": "语言",
        "kicker": "适用于 iPhone 和 iPad 的安静涂色 App",
        "title": "ChromaLilt",
        "description": "ChromaLilt 是一款轻松的涂色 App，支持 Hold to Bloom 长按上色、智能边缘画笔、本地进度保存和安静的色彩日记。",
        "lead": "在结构化线稿区域中长按，让颜料慢慢绽开。切换到边缘裁切画笔补充柔和笔触，完成作品后保存到 Color Journal。",
        "download": "前往 App Store 下载",
        "preview_label": "ChromaLilt 涂色预览",
        "stat_one": "长按绽色",
        "stat_two": "智能边缘画笔",
        "stat_three": "色彩日记",
        "section_features": "为短时间、低压力的涂色片刻设计",
        "feature_1_title": "长按生成柔和色彩",
        "feature_1": "在区域内长按即可生成水彩般的渐变色块，不会溢出线稿。",
        "feature_2_title": "沿边界安心涂抹",
        "feature_2": "智能画笔会把笔触限制在当前图形里，让页面保持干净。",
        "feature_3_title": "保存每一页进度",
        "feature_3": "进度本地保存，完成的作品会进入日记，也可以导出图片分享。",
        "section_art": "内置初始涂色图",
        "art_copy": "从小星球、花朵、舒适房间细节和放松图案开始。每张图都适配 ChromaLilt 的绽色和画笔工具。",
        "guide_title": "需要帮助？",
        "guide_copy": "先了解核心手势、导出流程和隐私模型，再开始第一张涂色页。",
        "footer": "ChromaLilt - 会绽放的安静涂色。",
        "help_title": "ChromaLilt 帮助",
        "help_desc": "了解 ChromaLilt 的 Hold to Bloom、智能边缘画笔、Color Journal 和图片导出。",
        "help_intro": "ChromaLilt 专注于缓慢、本地、低压力的涂色体验。从 Gallery 选择作品和情绪色盘，然后用绽色或画笔上色。",
        "help_steps": [
            ("开始一页", "打开 Gallery，选择 Daily Bloom 或任意初始作品。"),
            ("Hold to Bloom", "在区域内长按，让颜料柔和扩散。"),
            ("使用画笔", "切换 Brush，在当前形状内绘制被裁切的柔和笔触。"),
            ("完成和导出", "标记完成后保存到 Color Journal，也可以导出图片分享。"),
        ],
        "support_title": "ChromaLilt 支持",
        "support_desc": "联系 ChromaLilt 支持，获取涂色、导出、日记或 App Store 相关帮助。",
        "support_body": "如需支持、反馈功能或报告问题，请通过邮件告诉我们设备型号、iOS 版本和问题描述。",
        "privacy_title": "ChromaLilt 隐私政策",
        "privacy_desc": "ChromaLilt 将涂色进度保存在本地，不需要账号。",
        "privacy_body": "ChromaLilt 被设计为本地、私密的涂色空间。涂色进度和日记状态保存在你的设备上，App 不需要账号。如果你联系支持，我们只会使用你提供的信息来回复请求。",
    },
}

FALLBACKS = {
    "zh-Hant": "zh-Hans",
    "ja": "en-US",
    "ko": "en-US",
    "de-DE": "en-US",
    "fr-FR": "en-US",
    "es-ES": "en-US",
}

TRANSLATED_OVERRIDES = {
    "zh-Hant": {
        "nav_home": "首頁", "nav_help": "說明", "nav_support": "支援", "nav_privacy": "隱私", "language": "語言",
        "kicker": "適用於 iPhone 和 iPad 的安靜塗色 App",
        "description": "ChromaLilt 是一款放鬆塗色 App，支援長按綻色、智慧邊緣畫筆、本機進度保存和安靜的色彩日記。",
        "lead": "在結構化線稿區域中長按，讓顏料慢慢綻開。切換到邊緣裁切畫筆補上柔和筆觸，完成作品後保存到 Color Journal。",
        "download": "前往 App Store 下載",
        "footer": "ChromaLilt - 會綻放的安靜塗色。",
    },
    "ja": {
        "nav_home": "ホーム", "nav_help": "ヘルプ", "nav_support": "サポート", "nav_privacy": "プライバシー", "language": "言語",
        "kicker": "iPhone と iPad のための静かなぬりえアプリ",
        "description": "ChromaLilt は、Hold to Bloom、スマートエッジブラシ、ローカル保存、Color Journal を備えたリラックスできるぬりえアプリです。",
        "lead": "線画の領域を長押しして、色がやわらかく広がるのを楽しめます。ブラシに切り替えると、形の内側だけに穏やかなストロークを重ねられます。",
        "download": "App Store でダウンロード",
        "footer": "ChromaLilt - 色が咲く静かなぬりえ。",
    },
    "ko": {
        "nav_home": "홈", "nav_help": "도움말", "nav_support": "지원", "nav_privacy": "개인정보", "language": "언어",
        "kicker": "iPhone 및 iPad용 차분한 컬러링 앱",
        "description": "ChromaLilt는 Hold to Bloom, 스마트 에지 브러시, 로컬 진행 저장, Color Journal을 제공하는 편안한 컬러링 앱입니다.",
        "lead": "구조화된 선화 영역을 길게 눌러 색이 부드럽게 번지게 하세요. 브러시로 전환하면 현재 모양 안에서만 차분한 스트로크를 그릴 수 있습니다.",
        "download": "App Store에서 다운로드",
        "footer": "ChromaLilt - 피어나는 차분한 컬러링.",
    },
    "de-DE": {
        "nav_home": "Start", "nav_help": "Hilfe", "nav_support": "Support", "nav_privacy": "Datenschutz", "language": "Sprache",
        "kicker": "Ruhige Ausmal-App für iPhone und iPad",
        "description": "ChromaLilt ist eine entspannende Ausmal-App mit Hold to Bloom, Smart Edge Brush, lokalem Fortschritt und einem stillen Color Journal.",
        "lead": "Drücke in strukturierte Linienkunst und sieh, wie Farbe weich aufblüht. Mit dem Pinsel bleiben sanfte Striche innerhalb der Form.",
        "download": "Im App Store laden",
        "footer": "ChromaLilt - ruhiges Ausmalen, das aufblüht.",
    },
    "fr-FR": {
        "nav_home": "Accueil", "nav_help": "Aide", "nav_support": "Assistance", "nav_privacy": "Confidentialité", "language": "Langue",
        "kicker": "Application de coloriage calme pour iPhone et iPad",
        "description": "ChromaLilt est une application de coloriage apaisante avec Hold to Bloom, pinceau à bords intelligents, progression locale et Color Journal.",
        "lead": "Appuyez dans une zone de dessin pour faire éclore la couleur. Le pinceau reste dans les contours pour des traits doux et propres.",
        "download": "Télécharger sur l'App Store",
        "footer": "ChromaLilt - le coloriage calme qui fleurit.",
    },
    "es-ES": {
        "nav_home": "Inicio", "nav_help": "Ayuda", "nav_support": "Soporte", "nav_privacy": "Privacidad", "language": "Idioma",
        "kicker": "App de colorear tranquila para iPhone y iPad",
        "description": "ChromaLilt es una app relajante para colorear con Hold to Bloom, pincel inteligente, progreso local y Color Journal.",
        "lead": "Mantén pulsada una zona del dibujo para que el pigmento florezca. Cambia al pincel para añadir trazos suaves dentro de cada forma.",
        "download": "Descargar en App Store",
        "footer": "ChromaLilt - colorear con calma y color que florece.",
    },
}

PAGES = {
    "index": "index.html",
    "help": "help.html",
    "support": "support.html",
    "privacy": "privacy-policy.html",
}


def copy_for(locale: str) -> dict[str, object]:
    data = dict(COPY.get(locale, COPY[FALLBACKS.get(locale, "en-US")]))
    data.update(TRANSLATED_OVERRIDES.get(locale, {}))
    data.setdefault("title", "ChromaLilt")
    return data


def rel_prefix(locale: str) -> str:
    return "../"


def url_for(locale: str, page: str) -> str:
    return f"{BASE_URL}/{locale}/{PAGES[page]}"


def hreflang_links(page: str) -> str:
    links = []
    for locale, hreflang, _ in LOCALES:
        links.append(f'  <link rel="alternate" hreflang="{hreflang}" href="{url_for(locale, page)}">')
    links.append(f'  <link rel="alternate" hreflang="x-default" href="{url_for("en-US", page)}">')
    return "\n".join(links)


def language_select(current: str, page: str) -> str:
    options = []
    for locale, _, label in LOCALES:
        selected = " selected" if locale == current else ""
        options.append(f'<option value="../{locale}/{PAGES[page]}"{selected}>{escape(label)}</option>')
    return "".join(options)


def head(locale: str, page: str, title: str, description: str) -> str:
    prefix = rel_prefix(locale)
    canonical = url_for(locale, page)
    return f"""<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{escape(description)}">
  <meta name="robots" content="index,follow">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE_URL}/images/app-icon.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{BASE_URL}/images/app-icon.png">
  <link rel="canonical" href="{canonical}">
{hreflang_links(page)}
  <link rel="apple-touch-icon" sizes="180x180" href="{prefix}favicon/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="32x32" href="{prefix}favicon/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="{prefix}favicon/favicon-16x16.png">
  <link rel="manifest" href="{prefix}favicon/site.webmanifest">
  <meta name="theme-color" content="#E85F86">
  <link rel="stylesheet" href="{prefix}style/base.css">
  <title>{escape(title)}</title>
</head>"""


def topbar(locale: str, page: str, c: dict[str, object]) -> str:
    prefix = rel_prefix(locale)
    return f"""<header class="topbar">
  <a class="brand" href="{prefix}{locale}/index.html" aria-label="ChromaLilt home">
    <img src="{prefix}favicon/apple-touch-icon.png" alt="">
    <span>ChromaLilt</span>
  </a>
  <nav class="nav" aria-label="Primary">
    <a href="{prefix}{locale}/index.html">{escape(str(c["nav_home"]))}</a>
    <a href="{prefix}{locale}/help.html">{escape(str(c["nav_help"]))}</a>
    <a href="{prefix}{locale}/support.html">{escape(str(c["nav_support"]))}</a>
    <a href="{prefix}{locale}/privacy-policy.html">{escape(str(c["nav_privacy"]))}</a>
    <label class="language-switch"><span>{escape(str(c["language"]))}</span><select aria-label="{escape(str(c["language"]))}" onchange="if (this.value) window.location.href=this.value">{language_select(locale, page)}</select></label>
  </nav>
</header>"""


def app_store_button(c: dict[str, object]) -> str:
    return f'<a class="button primary" href="{APP_STORE_URL}"><img class="store-icon" src="../images/app-store-icon.svg" alt="">{escape(str(c["download"]))}</a>'


def layout(locale: str, page: str, title: str, description: str, body: str) -> str:
    c = copy_for(locale)
    return f"""<!DOCTYPE html>
<html lang="{locale}">
{head(locale, page, title, description)}
<body>
  <div class="page">
    <div class="container">
      {topbar(locale, page, c)}
      {body}
      <footer class="footer">{escape(str(c["footer"]))}</footer>
    </div>
  </div>
</body>
</html>
"""


def landing(locale: str) -> str:
    c = copy_for(locale)
    body = f"""<main>
  <section class="hero">
    <div class="hero-copy">
      <p class="kicker">{escape(str(c["kicker"]))}</p>
      <h1>ChromaLilt</h1>
      <p class="lead">{escape(str(c["lead"]))}</p>
      <div class="actions">{app_store_button(c)}<a class="button" href="help.html">{escape(str(c["nav_help"]))}</a></div>
    </div>
    <div class="product-panel" aria-label="{escape(str(c["preview_label"]))}">
      <div class="phone-preview">
        <div class="phone-top"></div>
        <div class="canvas-card">
          <div class="sun"></div>
          <div class="flower flower-a"></div>
          <div class="flower flower-b"></div>
          <div class="flower flower-c"></div>
        </div>
        <div class="tool-pills"><span>{escape(str(c["stat_one"]))}</span><span>{escape(str(c["stat_two"]))}</span></div>
      </div>
      <div class="panel-stats"><span>{escape(str(c["stat_one"]))}</span><span>{escape(str(c["stat_two"]))}</span><span>{escape(str(c["stat_three"]))}</span></div>
    </div>
  </section>
  <section class="section">
    <h2>{escape(str(c["section_features"]))}</h2>
    <div class="feature-grid">
      <article class="feature"><strong>{escape(str(c["feature_1_title"]))}</strong><p>{escape(str(c["feature_1"]))}</p></article>
      <article class="feature"><strong>{escape(str(c["feature_2_title"]))}</strong><p>{escape(str(c["feature_2"]))}</p></article>
      <article class="feature"><strong>{escape(str(c["feature_3_title"]))}</strong><p>{escape(str(c["feature_3"]))}</p></article>
    </div>
  </section>
  <section class="section split">
    <div><h2>{escape(str(c["section_art"]))}</h2><p>{escape(str(c["art_copy"]))}</p></div>
    {app_store_button(c)}
  </section>
  <section class="section split">
    <div><h2>{escape(str(c["guide_title"]))}</h2><p>{escape(str(c["guide_copy"]))}</p></div>
    <a class="button compact" href="help.html">{escape(str(c["nav_help"]))}</a>
  </section>
</main>"""
    return layout(locale, "index", f"ChromaLilt | {c['kicker']}", str(c["description"]), body)


def help_page(locale: str) -> str:
    c = copy_for(locale)
    steps = "".join(f"<article class=\"feature\"><strong>{escape(title)}</strong><p>{escape(text)}</p></article>" for title, text in c["help_steps"])
    body = f"""<main class="content-page">
  <section class="section">
    <p class="kicker">{escape(str(c["nav_help"]))}</p>
    <h1>{escape(str(c["help_title"]))}</h1>
    <p class="lead">{escape(str(c["help_intro"]))}</p>
  </section>
  <section class="section"><div class="feature-grid two">{steps}</div></section>
  <section class="section split"><div><h2>{escape(str(c["download"]))}</h2><p>{escape(str(c["description"]))}</p></div>{app_store_button(c)}</section>
</main>"""
    return layout(locale, "help", str(c["help_title"]), str(c["help_desc"]), body)


def support_page(locale: str) -> str:
    c = copy_for(locale)
    body = f"""<main class="content-page">
  <section class="section">
    <p class="kicker">{escape(str(c["nav_support"]))}</p>
    <h1>{escape(str(c["support_title"]))}</h1>
    <p class="lead">{escape(str(c["support_body"]))}</p>
    <div class="actions"><a class="button primary" href="mailto:cameoshell09@gmail.com?subject=ChromaLilt%20Support">cameoshell09@gmail.com</a></div>
  </section>
</main>"""
    return layout(locale, "support", str(c["support_title"]), str(c["support_desc"]), body)


def privacy_page(locale: str) -> str:
    c = copy_for(locale)
    body = f"""<main class="content-page">
  <section class="section">
    <p class="kicker">{escape(str(c["nav_privacy"]))}</p>
    <h1>{escape(str(c["privacy_title"]))}</h1>
    <p class="lead">{escape(str(c["privacy_body"]))}</p>
  </section>
  <section class="section">
    <h2>App Store</h2>
    <p>{escape(str(c["privacy_desc"]))}</p>
  </section>
</main>"""
    return layout(locale, "privacy", str(c["privacy_title"]), str(c["privacy_desc"]), body)


def root_index() -> str:
    return root_redirect("index")


def root_redirect(page: str) -> str:
    filename = PAGES[page]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="refresh" content="0; url=en-US/{filename}">
  <meta name="description" content="{COPY['en-US']['description']}">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{BASE_URL}/en-US/{filename}">
{hreflang_links(page)}
  <title>ChromaLilt</title>
</head>
<body><p><a href="en-US/{filename}">ChromaLilt</a></p></body>
</html>
"""


def write_static_files() -> None:
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n", encoding="utf-8")
    urls = [f"{BASE_URL}/index.html"]
    for locale, _, _ in LOCALES:
        for page in PAGES.values():
            urls.append(f"{BASE_URL}/{locale}/{page}")
    sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
    sitemap += "\n".join(f"  <url><loc>{url}</loc></url>" for url in urls)
    sitemap += "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    manifest = """{
  "name": "ChromaLilt",
  "short_name": "ChromaLilt",
  "icons": [
    { "src": "/favicon/apple-touch-icon.png", "sizes": "180x180", "type": "image/png" },
    { "src": "/images/app-icon.png", "sizes": "1024x1024", "type": "image/png" }
  ],
  "theme_color": "#E85F86",
  "background_color": "#FFF7F1",
  "display": "standalone"
}
"""
    (ROOT / "favicon" / "site.webmanifest").write_text(manifest, encoding="utf-8")


def main() -> None:
    (ROOT / "index.html").write_text(root_index(), encoding="utf-8")
    for page, filename in PAGES.items():
        if page != "index":
            (ROOT / filename).write_text(root_redirect(page), encoding="utf-8")
    for locale, _, _ in LOCALES:
        directory = ROOT / locale
        directory.mkdir(exist_ok=True)
        (directory / "index.html").write_text(landing(locale), encoding="utf-8")
        (directory / "help.html").write_text(help_page(locale), encoding="utf-8")
        (directory / "support.html").write_text(support_page(locale), encoding="utf-8")
        (directory / "privacy-policy.html").write_text(privacy_page(locale), encoding="utf-8")
    write_static_files()


if __name__ == "__main__":
    main()
