AUTHOR = "Alfarizi"
SITENAME = "Alphablog"
SITEURL = ""
SITESUBTITLE = "My personal blogging website"
THEME = "./themes/clean_blog/"
DISQUS_SITENAME = "alphablog-2"
COLOR_SCHEME_CSS = "monokai.css"
AVATAR_AUTHOR_EMAIL = "farizi1906@gmail.com"

PATH = "content"
STATIC_PATHS = ["images"]

HEADER_COVER = "images/post1_cover.jpg"

DEFAULT_DATE_FORMAT = ('%d %b %Y')
TIMEZONE = "Asia/Jakarta"
DEFAULT_DATE = "fs"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Blogroll
MENUITEMS = (("About", "pages/about.html"),
             ("Categories", "/categories.html"),)

# Social widget
GITHUB_URL = "https://github.com/alphabeta1906"

SOCIAL = (("github", GITHUB_URL),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True