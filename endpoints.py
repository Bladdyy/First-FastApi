from typing import List

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/tags")
def all_tags(db: Session = Depends(get_db)):
    '''
    Returns all tag names with number of images connected to them.
    '''
    return {'tags': [{"tag": tag.name, "number_of_images": len(tag.images)} for tag in db.query(models.Tag).all()]}


@app.get("/images")
def all_images(db: Session = Depends(get_db)):
    '''
    Returns all images and tags connected to them.
    '''
    images = (db.query(models.Image)
              .all())
    json = {}
    for image in images:
        tags = [{"tag": tag.name} for tag in image.tags]
        json.update({image.name: tags})
    return json


@app.delete("/images/del")
def delete_images(imgs: List[int], db: Session = Depends(get_db)):
    '''
    Delete all images with given id's.
    **Image's id should be in json format:** {"images": [*IDs HERE*]}.
    '''
    db.query(models.Image).filter(models.Image.id.in_(imgs)).delete()
    db.commit()
    return {"answer": True}


@app.get("/images/{tag_name}")
def get_tagged_images(tag_name: str, db: Session = Depends(get_db)):
    """
    Retruns all names of images connected to given tag.
    """
    tag = ((db.query(models.Tag)
           .filter(models.Tag.name == tag_name))
           .first())

    if tag is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {tag_name} : Does not exist"
        )

    return {tag.name: [{"image": image.name} for image in tag.images]}


@app.post("/create")
def create(db: Session = Depends(get_db)):
    tag1 = models.Tag(name="fajny")
    tag2 = models.Tag(name="pies")
    tag3 = models.Tag(name="LubieProstokąty")

    image1 = models.Image(name="Kwadrat")
    image2 = models.Image(name="Pies")
    image3 = models.Image(name="Krzaczek")
    image4 = models.Image(name="Kłębuszek")

    image3.tags = [tag1, tag3]
    image2.tags = [tag1, tag2, tag3]
    image4.tags = [tag1]

    db.add_all([tag1, tag2, tag3, image1, image2, image3, image4])
    db.commit()
    return {"answer": True}


