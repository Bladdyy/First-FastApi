from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


image_tags = Table('image_tags', Base.metadata,
                   Column('tag_id', ForeignKey('tags.id'), primary_key=True),
                   Column('image_id', ForeignKey('images.id'), primary_key=True)
                   )


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    images = relationship("Image", secondary="image_tags", back_populates='tags')


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    tags = relationship("Tag", secondary="image_tags", back_populates='images')
