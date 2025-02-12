import os
import sys
from typing import List 
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship, DeclarativeBase
from eralchemy2 import render_er
from sqlalchemy import ForeignKey, String, create_engine, Column, Table, Integer

Base = declarative_base()


follower = Table(
    "follower",
    Base.metadata,
    Column("user_from_id", ForeignKey("user.id")),
    Column("user_to_id", ForeignKey("user.id")),
)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    comment: Mapped[List["Comment"]] = relationship(back_populates="user")
    post: Mapped[List["Post"]] = relationship(back_populates="user") 

    



class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id")) 
    post: Mapped["Post"] = relationship(back_populates="media")   

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id")) 
    user: Mapped["User"] = relationship(back_populates="comment") 
    media: Mapped[List["Media"]] = relationship(back_populates="post")  

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(80), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))    
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))    
    user: Mapped["User"] = relationship(back_populates="comment")
 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
