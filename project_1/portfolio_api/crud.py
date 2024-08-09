from fastapi import Depends, FastAPI, HTTPException, status
from . import models


def get_project(project_id: int, db: Session):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project with id {project_id} not found")
    return project

db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


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
    return
