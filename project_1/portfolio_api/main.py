from fastapi import FastAPI, Depends, HTTPException
from . import models, schemas, crud
from .database import local_session, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_session():
    db = local_session()
    try:
        yield db
    finally:
        db.close()

#Project endpoints
@app.post("/projects/", status_code=status.HTTP_201_CREATED)
def project(Projectcreate: schemas.ProjectCreate, db: Session = Depends(get_session)):
    new_project = crud.create_project(Session, Projectcreate)
            return new_project


@app.get("/projects/", response_model=list[schemas.Project])
def get_projects(db: Session = Depends(get_session)):
    projects = db.query(models.Project).all()
    return projects

@app.get("/projects/{project_id}", response_model=schemas.Project)
def get_project_by_id(project_id: int, Session = Depends(get_session)):
    project = get_project(project_id, Session)
    return project


@app.delete("/projects/{project_id}")
def delete_project_endpoint(project_id: int, db: Session = Depends(get_session)):
            delete_project(Session, project_id)
            return {"message": "Project deleted successfully"}



#Blog post endpoints

@app.post("/blog_posts/", status_code=status.HTTP_201_CREATED)
def create_blog_post(blog_post: schemas.BlogPostCreate, Session = Depends(get_dession)):
new_blog_post = crud.BlogPost(Session, BlogPostCreate)
 return new_blog_post

@app.get("/blog_posts/", response_model=list[schemas.BlogPost])
def get_blog_posts(Session = Depends(get_sessiom)):
    blog_posts = db.query(models.BlogPost).all()
    return blog_posts

@app.get("/blog_posts/{blog_post_id}", response_model=schemas.BlogPost)
def get_blog_post_by_id(blog_post_id: int, Session = Depends(get_db)):
    blog_post = get_blog_post(blog_post_id, Session)
    return blog_postp

@app.put("/blog_posts/{blog_post_id}")
def update_blog_post(blog_post_id: int, blog_post_update: schemas.BlogPostCreate, Session = Depends(get_session)):
    blog_post = get_blog_post(blog_post_id, db)
    return blog_post

@app.delete("/blog_posts/{blog_post_id}")
def delete_blog_post(blog_post_id: int, Session = Depends(get_session)):
    blog_post = get_blog_post(blog_post_id, db)
    db.delete(blog_post)
     return {"message": "Blog post deleted successfully"}


# Contact endpoints
@app.post("/contacts/", status_code=status.HTTP_201_CREATED)
def create_contact(contact: schemas.ContactCreate, Session = Depends(get_session)):
     new_contact = crud.create_context(Session, contact)
     return new_contact

 @app.get("/contacts/", response_model=list[schemas.Contact])
def get_contacts(Session = Depends(get_session)):
contacts = db.query(models.Contact).all()
    return contacts

@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact_update: schemas.ContactCreate, Session = Depends(get_session)):
    contact = get_contact(contact_id, Session)
    return contact

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int, Session = Depends(get_session)):
    contact = get_contact(contact_id, Session)
    return {"message": "Contact deleted successfully"}
