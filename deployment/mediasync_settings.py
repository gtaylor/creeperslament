"""
This module determines how to combine various JS/CSS files into monolithic,
minified, compressed chunks. This cuts down page load time drastically,
and saves us a lot of bandwidth.

There are also a number of mediasync-related settings in the MEDIASYNC dict
at the bottom of this module. This dict is imported by the various 
settings/staging_settings/prod_settings modules.
"""
import os

# NOTE: Not sure if the quirk noted with the massive JS combo files applies
# for CSS. Make sure that CSS still loads and renders correctly after adding
# more files to this one.
CSS_JOINED_BASE1 = [
    'css/reset-min.css',
    'css/base.css',
    'css/font_candal.css',
]

# Here is where it is all tied together. The various settings modules import
# this, for the sake of consistency and not repeating ourselves.
JOINED_MEDIA = {
    'css/joined_base.css': CSS_JOINED_BASE1,
}

# Tacked on to the end of various URLs to cache bust.
GIT_COMMIT_HASH_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.git', 'ORIG_HEAD')
GIT_COMMIT_HASH = open(GIT_COMMIT_HASH_FILE, 'r').read().strip()
# Tacked on to the end of various URLs to cache bust.
MEDIA_CACHE_BUSTER = GIT_COMMIT_HASH[:20]

# This is used for syncing the /media directory with S3.
MEDIASYNC = {
    'BACKEND': 'mediasync.backends.s3',
    # When this is True, force serving media from S3.
    #'SERVE_REMOTE': True,
    #'AWS_KEY': AWS_ACCESS_KEY_ID,
    #'AWS_SECRET': AWS_SECRET_ACCESS_KEY,
    #'AWS_BUCKET': 'creeperslament',
    # The following entries combine CSS and JavaScript files, and minify them as well.
    'JOINED': JOINED_MEDIA,
    'CACHE_BUSTER': MEDIA_CACHE_BUSTER,
    'DOCTYPE': 'html5',
    'PROCESSORS': ('mediasync.processors.css_minifier',),
}
