from django.conf import settings
from django.http import StreamingHttpResponse
from django.core.files.storage import get_storage_class


def emberapp(request):
    # The Ember frontend SPA index file
    # By getting the storage_class like this, we guarantee that this will work
    #   no matter what backend is used for serving static files
    #   Which means, this will work both in development and production
    #   Make sure to run collectstatic (even in development)
    # TODO: how to use this in development without being forced to run collectstatic?
    storage_class = get_storage_class(settings.STATICFILES_STORAGE)
    index_file = storage_class().open(settings.FE_INDEX_HTML)
    return StreamingHttpResponse(index_file)
