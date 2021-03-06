import os

SETTINGS = {
    'SITENAME': 'Imperial College Caving Club',
    'SOURCE_FOLDER': os.path.join('{{ BASE_FOLDER }}', 'content'),
    'OUTPUT_FOLDER': os.path.join('{{ BASE_FOLDER }}', 'output'),
    'OUTPUT_CSS_FOLDER': os.path.join('{{ OUTPUT_FOLDER }}', 'theme', 'css'),
    'OUTPUT_JS_FOLDER': os.path.join('{{ OUTPUT_FOLDER }}', 'theme', 'js'),
    'ARTICLE_TYPES': ['trip', 'tour'],
    'INDEX_TYPES': ['index', 'stickyindex'],
    'PLUGINS': ['inlinephotos', 'acyear', 'cavepeeps', 'indexcachetype', 'photoarchive', 'metainserter', 'oldurl', 'wiki', 'strikethrough'],
    'NO_SCAN': ['wiki','caves','cavers'],
    'PHOTO_LOCATION': 'https://union.ic.ac.uk/rcc/caving/photo_archive/',
    'ASSET_LOCATION': 'https://union.ic.ac.uk/rcc/caving/assets/',
    'FAVICON': 'assets/iclogo.png',
    'SITEURL': "",
    'PHOTOREEL': True,
    'PHOTOREEL_NUM_ARTICLES': 6,
    "BADGES": {
        'lightning': {
            'src': 'lightning.png',
            'alt': 'In the bivi'
        }
    },
    "WRITE_TRIGGERS": {
        "ARTICLE": ["ARTICLE.NEW_FILE", "ARTICLE.REMOVED_FILE"],
        "PAGE":  ["ARTICLE.NEW_FILE", "ARTICLE.REMOVED_FILE"],
        "INDEX": ["ARTICLE.NEW_FILE", "ARTICLE.REMOVED_FILE", "INDEX_ARTICLE.CONTENT_CHANGE", "INDEX_ARTICLE.NEW_FILE", "INDEX_ARTICLE.REMOVED_FILE"],
        "INDEX_ARTICLE": ["ARTICLE.NEW_FILE", "ARTICLE.REMOVED_FILE", "INDEX_ARTICLE.CONTENT_CHANGE", "INDEX_ARTICLE.NEW_FILE", "INDEX_ARTICLE.REMOVED_FILE"],
        "WIKI": ["ARTICLE.NEW_FILE", "ARTICLE.REMOVED_FILE"]
    },
    "META_WRITE_TRIGGERS": {
        "ARTICLE": ['title', 'location', 'date', 'status', 'summary'],
        "PAGE": ['title', 'location', 'date', 'status'],
        "INDEX": ["title", "date", "location", "thumbr", "thumbl", "summary", "status"],
        "INDEX_ARTICLE": ["title", "date", "location", "thumbr", "thumbl", "summary", "status"],
        "WIKI": ['title', 'location', 'date', 'status', 'summary']
    },
    "SUBSITES": {
        "newzealand": {
            'PLUGINS': ['inlinephotos', 'photoarchive', 'metainserter'],
            'TEMPLATES_FOLDER': os.path.join('{{ BASE_FOLDER }}', 'theme', 'templates', 'subsites', 'newzealand'),
            'CSS_FOLDER': os.path.join('{{ BASE_FOLDER }}', 'theme', 'static', 'subsites', 'newzealand', 'css'),
            'JS_FOLDER': os.path.join('{{ BASE_FOLDER }}', 'theme', 'static', 'subsites', 'newzealand', 'js'),            
            'OUTPUT_CSS_FOLDER': os.path.join('{{ OUTPUT_FOLDER }}', 'theme', 'subsites', 'newzealand', 'css'),
            'OUTPUT_JS_FOLDER': os.path.join('{{ OUTPUT_FOLDER }}', 'theme', 'subsites', 'newzealand', 'js'),
            'ARTICLE_TYPES': [None],
            'BASEURL': '',
            'SITEURL': "/newzealand",
            'PHOTOREEL': False,
            'ARTICLE_SLUG': '{basename}.html',
            'PAGE_SLUG': '{basename}.html'
        },
        "slovenia" : {
            'PLUGINS': ['inlinephotos', 'photoarchive', 'metainserter'],
            'TEMPLATES_FOLDER': os.path.join('{{ BASE_FOLDER }}', 'theme', 'templates', 'subsites', 'slovenia'),
            'CSS_FOLDER': os.path.join('{{ BASE_FOLDER }}', 'theme', 'static', 'subsites', 'slovenia', 'css'),
            'JS_FOLDER': os.path.join('{{ BASE_FOLDER }}', 'theme', 'static', 'subsites', 'slovenia', 'js'),            
            'OUTPUT_CSS_FOLDER': os.path.join('{{ OUTPUT_FOLDER }}', 'theme', 'subsites', 'slovenia', 'css'),
            'OUTPUT_JS_FOLDER': os.path.join('{{ OUTPUT_FOLDER }}', 'theme', 'subsites', 'slovenia', 'js'),
            'ARTICLE_TYPES': ['expedition'],
            'BASEURL': '',
            'SITEURL': "/slovenia",
            'PHOTOREEL': False,
            'ARTICLE_SLUG': '{date}-{location}.html'
        }
    }
}
