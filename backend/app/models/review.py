from sqlalchemy import inspect
from sqlalchemy.orm.properties import ColumnProperty

from . import db
from .budget_enum import budget_enum

# common columns and methods across multiple data models can be added via a Mixin class:
# https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html

# see examples of Mixins in current and past Blueprint projects:
# https://github.com/uwblueprint/dancefest-web/blob/master/db/models.py#L10-L70
# https://github.com/uwblueprint/plasta/blob/master/backend/app/models/mixins.py#L10-L95

class Review(db.Model):
    # define the reviewer table

    __tablename__ = 'review'

    id = db.column(db.Integer, primary_key=True, nullable=False)
    content = db.column(db.String, nullable=False)
    # reviewer_id = db.column(db.Integer, db.ForeignKey('reviewers.id'))
    # reviewer = db.relationship('Reviewer', back_populates='review')
