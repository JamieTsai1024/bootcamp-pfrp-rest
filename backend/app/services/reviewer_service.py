from ..models import db
from ..models.reviewer import Reviewer

'''
while our business logic is really simple so far, it is beneficial to keep it apart from the controller logic.
separation of concerns leads to maintainable code as the application grows, and also makes the code easier to unit test
'''

def delete_reviewer(id):
    deleted = Reviewer.query.filter_by(id=id).delete()
    # TODO: Delete reviews
    db.session.commit()
    
    # deleted is the number of rows deleted
    if deleted == 1:
        return id
    return None
