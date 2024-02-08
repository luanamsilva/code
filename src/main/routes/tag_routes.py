from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

tag_routes =  Blueprint('tag_routes', __name__)

@tag_routes.route('/create', methods=['POST'])
def create_tag():
    tag_creator_view = TagCreatorView()
    http_request = HttpRequest(body=request.json)

    response = tag_creator_view.validate_and_create(http_request)

    return jsonify(response.body), response.status_code