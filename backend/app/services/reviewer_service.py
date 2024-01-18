from ..models import db
from ..models.reviewer import Reviewer

'''
while our business logic is really simple so far, it is beneficial to keep it apart from the controller logic.
separation of concerns leads to maintainable code as the application grows, and also makes the code easier to unit test
'''

def get_reviewers():
    # Reviewer is a SQLAlchemy model, we can use convenient methods provided
    # by SQLAlchemy like query.all() to query the data
    return [result.to_dict() for result in Reviewer.query.all()]


def get_reviewer(id):
    # get queries by the primary key, which is id for the Reviewer
    reviewer = Reviewer.query.get(id)
    if reviewer is None:
        return reviewer
    return reviewer.to_dict()

def delete_reviewer(id):
    deleted = Reviewer.query.filter_by(id=id).delete()
    # TODO: Delete reviews
    db.session.commit()
    
    # deleted is the number of rows deleted
    if deleted == 1:
        return id
    return None
