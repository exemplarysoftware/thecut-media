import sys
import os

try:
    from django.conf import settings
    from django.test.utils import get_runner

    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        ROOT_URLCONF="test_app.urls",
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "thecut.media",
            "thecut.media.mediasources",
            "thecut.media.galleries",
            "test_app",
            "sorl.thumbnail",
            "taggit",
        ],
        SITE_ID=1,
        MIDDLEWARE_CLASSES=(),
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'OPTIONS': {
                    'loaders': [
                        ('django.template.loaders.cached.Loader',
                         ['django.template.loaders.filesystem.Loader',
                          'django.template.loaders.app_directories.Loader'])
                    ],
                },
            },
        ],
        # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
        BASE_DIR = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'thecut-media'),
    )

    try:
        import django
        setup = django.setup
    except AttributeError:
        pass
    else:
        setup()

except ImportError:
    import traceback
    traceback.print_exc()
    msg = "To fix this error, run: pip install -r requirements-test.txt"
    raise ImportError(msg)


def run_tests(*test_args):
    if not test_args:
        test_args = ['thecut.media.tests', 'thecut.media.galleries.tests',
                     'thecut.media.mediasources.tests']

    # Run tests
    TestRunner = get_runner(settings)
    test_runner = TestRunner()

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(bool(failures))


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
