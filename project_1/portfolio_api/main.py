from fastapi import FastAPI, Depends, HTTPException
from . import models, schemas, crud
from .database import local_session, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()

#Project endpoints

@app.post("/project")
def project(Projectcreate:schemas.Projectcreate,session=Depends(get_session):
            new_project = crud.create_project(session, Projectcreate)
            return new_project


@app.post("/projects/", status_code=status.HTTP_201_CREATED)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    new_project = models.Project(**project.dict())

@app.get("/projects/", response_model=list[schemas.Project])
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(models.Project).all()
    return projects

@app.get("/projects/{project_id}", response_model=schemas.Project)
def get_project_by_id(project_id: int, db: Session = Depends(get_db)):
    project = get_project(project_id, db)
    return project


Blog post endpoints

Contact endpoints

