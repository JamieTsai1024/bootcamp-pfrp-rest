from flask import Blueprint, jsonify, request

from ..resources.restaurant_resource import RestaurantResource
from ..services import reviewer_service

# this is the controller layer of the application (MVC), it is only responsible for receiving requests and sending responses
# it should be kept lean, all business logic belongs in the service layer

# defines a shared URL prefix for all routes
blueprint = Blueprint('reviewer', __name__, url_prefix='/reviewer')

# defines GET endpoint for retrieving all reviewers
@blueprint.route('/', methods=['GET'], strict_slashes=False)
def get_reviewers():
    # restaurant_service does the actually fetching of reviewers
    result = reviewer_service.get_reviewers()
    # HTTP status code 200 means OK
    return jsonify(result), 200


# defines GET endpoint for retrieving a single reviewer based on a provided id
@blueprint.route('/<int:id>', methods=['GET'], strict_slashes=False)
def get_reviewer(id):
    result = reviewer_service.get_reviewer(id)
    if result is None:
        error = {'error': 'reviewer not found'}
        # HTTP status code 404 means Not Found
        return jsonify(error), 404

    # HTTP status code 200 means OK
    return jsonify(result), 200

# defines DELETE endpoint for deleting the restaurant with the provided id
@blueprint.route('/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete_reviewer(id):
    result = reviewer_service.delete_reviewer(id)

    if result is None:
        error = {'error': 'restaurant not found'}
        return jsonify(error), 404
    
    return jsonify(result), 200
