from __future__ import unicode_literals

from django.conf import settings  # noqa

from appconf import AppConf


def is_installed(package):
    try:
        __import__(package)
        return True
    except ImportError:
        return False


class PinaxBlogAppConf(AppConf):

    ALL_SECTION_NAME = "all"
    SECTIONS = []
    UNPUBLISHED_STATES = [
        "Draft"
    ]
    FEED_TITLE = "Blog"
    SECTION_FEED_TITLE = "Blog (%s)"
    SLUG_UNIQUE = False
    PAGINATE_BY = 10

    class Meta:
        prefix = "pinax_blog"
