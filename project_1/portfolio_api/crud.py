 from . import models


def create_project(session, Projectcreate):
    new_project = models.Project(title=Projectcreate.title, description=Projectcreate.description, image_uri=Projectcreate.image_url, link= Projectcreate.link)

    Session.add(new_project)
    Session.commit()
    Session.refresh(new_project)

    return new_project


    def update_project_logic(project_id: int, project_update: schemas.ProjectCreate, Session):
    project = get_project(project_id, Session)
    project.title = project_update.title
    project.description = project_update.description
    project.image_url = project_update.image_url
    project.link = project_update.link
    Session.commit()
    Session.refresh(project)
    return project


def delete_project(Session, project_id: int):
    project = get_project(Session, project_id)
    Session.delete(project)
    Session.commit()


def create_blog_post(BlogPostCreate, Session):
    new_blog_post = models.BlogPost(title=BlogPostCreate.title, content=BlogPostCreate.content, image_url=BlogPoatCreate.content, created_at=BlogPostCreate.created_at)
    Session.add(new_blog_post)
    Session.commit()
    Session.refresh(new_blog_post)
    
    return new_blog_post

def update_blog_post(BlogPostCreate, Session):
     blog_post = get_blog_post(blog_post_id, Session)
    blog_post.title = blog_post_update.title
    blog_post.content = blog_post_update.content
    blog_post.image_url = blog_post_update.image_url
    blog_post.created_at = blog_post_update.created_at
    Session.commit()
    Session.refresh(blog_post)
    return blog_post

def delete_blog_post(blog_post_id: int, Session):
    blog_post = get_blog_post(blog_post_id, Session)
    Session.delete(blog_post)
    Session.commit()
    return blog_post

def create_contact(contact: schemas.ContactCreate, Session = Depends(get_session)):
    new_contact = models.Contact(**contact.dict())
    session.add(new_contact)
    session.commit()
    session.refresh(new_contact)
    return new_contact

def update_contact(contact_id: int, contact_update: schemas.ContactCreate, Session = Depends(get_session)):
    contact = get_contact(contact_id, session)
    contact.name = contact_update.name
    contact.email = contact_update.email
    contact.message = contact_update.message
    sessiom.commit()
    session.refresh(contact)
    return contact

def delete_contact(contact_id: int, Session = Depends(get_session)):
    contact = get_contact(contact_id, session)
    session.delete(contact)
    session.commit()
    return contact

