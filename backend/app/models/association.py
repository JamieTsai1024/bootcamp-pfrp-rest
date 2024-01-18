from . import db

restaurant_group_association = db.Table('restaurant_group',
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'), primary_key=True),
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id'), primary_key=True)
)