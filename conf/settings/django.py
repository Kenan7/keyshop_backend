import environ

root = environ.Path(__file__) - 3  # get root of the project
env = environ.Env()
environ.Env.read_env()  # reading .env file

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = root()


CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": env.db(),
}

GRAPH_MODELS = {
    "pygraphviz": True,
    "group_models": True,
    "exclude_models": "BasePasscode, AbstractBaseUser, PermissionsMixin, Group, Permission, Session, ContentType, AbstractBaseSession, LogEntry",
}

DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_PROJECT_ID = "keyshop"
GS_BUCKET_NAME = GS_PROJECT_ID
GS_MEDIA_BUCKET_NAME = "keyshop/media"

MEDIA_URL = "https://storage.googleapis.com/{}/".format(GS_MEDIA_BUCKET_NAME)


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core.apps.CoreConfig",
    "product.apps.ProductConfig",
    "contact_form.apps.ContactFormConfig",
    "order.apps.OrderConfig",
    "rest_framework",
    "djoser",
    "drf_yasg",
    "corsheaders",
    "django_extensions",
    "django_filters",
    "debug_toolbar",
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "conf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "conf.wsgi.application"

AUTH_USER_MODEL = "core.CustomUser"

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

public_root = root.path("public/")

STATIC_ROOT = public_root("static")
STATIC_URL = env.str("STATIC_URL", default="/public/static/")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# GS_STATIC_BUCKET_NAME = "keyshop/static"
# STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
# STATIC_URL = "https://storage.googleapis.com/{}/".format(GS_STATIC_BUCKET_NAME)
