from sqlalchemy import Integer
from app import db
from sqlalchemy.orm import Session, Mapped, mapped_column


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    status = db.Column(db.String(50), default='incompleta')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate= db.func.current_timestamp())

    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status
        
    def __repr__(self):
        return f"<Task %r>" % self.title
    
    def create_task(title, description =None, status=''):
        new_task = Task(title=title, description=description, status=status)
        db.session.add(new_task)
        db.session.commit()
        return new_task
        
    def get_all_tasks():
        return Task.query_all()

    def update_task():
        pass

    def delete_task():
        pass
    