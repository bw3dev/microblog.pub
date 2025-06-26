import os
from app.customization import register_html_page

for page in os.scandir('data/pages'):
  if page.is_file() and page.name.endswith('.html'):
    basename, ext = os.path.splitext(page.name)
    pagename, nav = os.path.splitext(basename)
    register_html_page(f"/{pagename}", title = pagename.capitalize(), html_file = f"pages/{page.name}", show_in_navbar = (nav != '.nonav'))
