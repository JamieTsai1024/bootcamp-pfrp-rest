from sqlalchemy import inspect
from sqlalchemy.orm.properties import ColumnProperty

from . import db
from .budget_enum import budget_enum
from .association import restaurant_group_association

# common columns and methods across multiple data models can be added via a Mixin class:
# https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html

# see examples of Mixins in current and past Blueprint projects:
# https://github.com/uwblueprint/dancefest-web/blob/master/db/models.py#L10-L70
# https://github.com/uwblueprint/plasta/blob/master/backend/app/models/mixins.py#L10-L95


class RestaurantGroup(db.Model):
    # define the groups table

    __tablename__ = 'restaurant_group'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250))
    restaurantIds = db.relationship('Restaurant', secondary=restaurant_group_association, back_populates='groups')

