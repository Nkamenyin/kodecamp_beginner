from pydantic import BaseModel

class ProjectCreate(BaseModel):
    title: str
    description: str
    image_url: str
    link: str

class Project(ProjectCreate):
    id: int

class BlogPostCreate(BaseModel):
    title: str
    content: str
    image_url: str
    created_at: str

class BlogPost(BlogPostCreate):
    id: int

class ContactCreate(BaseModel):
    name: str
    email: str
    message: str

class Contact(ContactCreate):
    id: int
