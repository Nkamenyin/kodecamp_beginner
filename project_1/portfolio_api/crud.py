from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

# ... other imports

def get_project(project_id: int, db: Session):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project with id {project_id} not found")
    return project

@app.post("/projects/", status_code=status.HTTP_201_CREATED)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    new_project = models.Project(**project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@app.get("/projects/", response_model=list[schemas.Project])
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(models.Project).all()
    return projects

@app.get("/projects/{project_id}", response_model=schemas.Project)
def get_project_by_id(project_id: int, db: Session = Depends(get_db)):
    project = get_project(project_id, db)
    return project

@app.put("/projects/{project_id}")
def update_project(project_id: int, project_update: schemas.ProjectCreate, db: Session = Depends(get_db)):
    project = get_project(project_id, db)
    project.title = project_update.title
    project.description = project_update.description
    project.image_url = project_update.image_url
    project.link = project_update.link
    db.commit()
    db.refresh(project)
    return project

@app.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = get_project(project_id, db)
    db.delete(project)
    db.commit()
    return {"message": "Project deleted successfully"}

