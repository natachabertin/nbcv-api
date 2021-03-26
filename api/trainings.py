from typing import List

import fastapi
from fastapi import Depends, Response
from sqlalchemy.orm import Session

from crud import trainings as crud
from dependencies.database import get_db
from schemas.trainings import Training, TrainingCreate, TrainingUpdate


router = fastapi.APIRouter()


@router.get('/', name='all_trainings', response_model=List[Training])
def get_trainings(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
        ) -> List[Training]:
    return crud.get_all(db, skip=skip, limit=limit)


@router.post('/', name='add_training', status_code=201, response_model=Training)
def create_training(training: TrainingCreate, db: Session = Depends(get_db)) -> Training:

    return crud.create(db=db, training=training)


@router.get('/{training_id}', name='get_training', response_model=Training)
def get_training(training_id: int, db: Session = Depends(get_db)) -> Training:
    db_training = crud.select_by_id(db, training_id=training_id)
    return db_training


@router.patch('/{training_id}', name='update_training', response_model=Training)
def update_training(training_id: int, training: TrainingUpdate, db: Session = Depends(get_db)) -> Training:
    return crud.update(db=db, training_id=training_id, training_submit=training)


@router.delete('/{training_id}', name='delete_training', status_code=204, response_class=Response)
def delete_training(training_id: int, db: Session = Depends(get_db)):
    return crud.delete(db=db, training_id=training_id)
