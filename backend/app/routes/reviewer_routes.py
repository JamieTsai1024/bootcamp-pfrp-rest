from flask import Blueprint, jsonify, request

from ..resources.restaurant_resource import RestaurantResource
from ..services import reviewer_service

# this is the controller layer of the application (MVC), it is only responsible for receiving requests and sending responses
# it should be kept lean, all business logic belongs in the service layer

# defines a shared URL prefix for all routes
blueprint = Blueprint('reviewer', __name__, url_prefix='/reviewer')

# defines DELETE endpoint for deleting the restaurant with the provided id
@blueprint.route('/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete_reviewer(id):
    result = reviewer_service.delete_reviewer(id)

    if result is None:
        error = {'error': 'restaurant not found'}
        return jsonify(error), 404
    
    return jsonify(result), 200
