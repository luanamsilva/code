from src.views.http_types.http_response import HttpResponse

def error_handler(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=500,
        body={
            "error": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
