AUTHOR = 'ZWL'
SITENAME = 'Weilei Zeng'
# SITEURL = "https://weileizeng.github.io"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Home·localhost:8000","http://localhost:8000"),
    ("Home·weileizeng.github.io","https://weileizeng.github.io/"),
    ("GitHub repo","https://github.com/WeileiZeng/weileizeng.github.io"),
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (
    ("GitHub/WeileiZeng","https://github.com/WeileiZeng"),
    ("WeChat·微信", "#"),
    ("Zhihu·知乎", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

#add by weilei
THEME="../zurb-F5-basic"

#add logo by modify theme file
SITE_FARICON="/images/logos/favicon.ico"
# SITELOGO="/images/logos/"
# SITE_LOGO="/images/logos/logo@96px.png"
# SITE_LOGO="/images/logos/zw@320px.png"
SITE_LOGO="/images/logos/zw@160px.png"
