from rest_framework_json_api.exceptions import exception_handler

def custom_exception_handler(exc, context):
    # DRF returns 400, but EmberData wants 422. I will force a 422 always.
    # See here:
    # - http://stackoverflow.com/q/34609797/647991
    # - http://stackoverflow.com/a/34609452/647991
    # Call the rest_framework_json_api's exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # TODO: is this correct? 422 in all exception cases?!
    response.status_code = 422
    return response
