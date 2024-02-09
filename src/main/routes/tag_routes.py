from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView
from src.error.error_handler import error_handler

tag_routes =  Blueprint('tag_routes', __name__)

@tag_routes.route('/create', methods=['POST'])
def create_tag():
    response = None
    try:
        tag_creator_view = TagCreatorView()
        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.validate_and_create(http_request)

    except Exception as exception:
        response = error_handler(exception)

    return jsonify(response.body), response.status_code
