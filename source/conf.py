# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# import sphinx_rtd_theme
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# import recommonmark

project = '何地置老夫'
copyright = '2021, 冯文成'
author = '冯文成'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



templates_path = ['_templates']
exclude_patterns = []

# language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
# html_theme = 'press'
# html_static_path = ['_static']

html_theme ='sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = 'logo.png' 
html_theme_options = {
    'logo_only': False,
    'display_version': False,
}

# extensions = ['recommonmark']

# from recommonmark.parser import CommonMarkParser
# source_parsers = {
#    '.md': CommonMarkParser,
#}
# source_suffix = ['.rst', '.md']


extensions = [
    # ... 数学公式扩展项
    'sphinx.ext.mathjax',  # 推荐，使用MathJax渲染
    # 或 'sphinx.ext.imgmath' （生成图片格式公式）
]


html_static_path = ['_static']

# 注册自定义 CSS
def setup(app):
    app.add_css_file('mycss.css')  # 加载创建的CSS文件



extensions = [
    # 其他扩展...
    'myst_parser'  # 确保这一行存在且无拼写错误
]



# 启用 MyST 的扩展功能（按需选择）
myst_enable_extensions = [
    "amsmath",        # 支持 LaTeX 公式（如 $E=mc^2$）
    "attrs_inline",   # 支持行内属性（如 `text {#id .class}`）
    "colon_fence",    # 支持 `:::` 作为代码块/容器的分隔符（替代 ```）
    "deflist",        # 支持定义列表（如 `术语\n: 解释`）
    "dollarmath",     # 支持 $ 包裹的行内公式和 $$ 包裹的块公式
    "fieldlist",      # 支持字段列表（如 `:姓名: 张三`）
    "html_admonition",# 支持 HTML 警告框（如 <div class="note">...</div>）
    "html_image",     # 支持 HTML 图片标签（如 <img src="..." />）
 #   "linkify",        # 自动将 URL 转换为链接（无需 []()）
    "replacements",   # 支持文本替换（如 --- → —）
    "smartquotes",    # 自动将直引号转换为弯引号（如 " → “”）
    "strikethrough",  # 支持删除线（如 ~~文本~~）
    "substitution",   # 支持变量替换（如 {{ var }}）
    "tasklist",       # 支持任务列表（如 - [x] 已完成）
]

