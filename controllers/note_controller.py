from flask import flash
from models import db
from models.note import Note


class NoteController:
    @staticmethod
    def list_note(page_number=1, per_page=10):
        try:
            notes=Note.query.paginate(page=page_number,per_page=per_page)
            return notes
        except Exception as e:
            print(e)
            return []
        
    @staticmethod
    def create_note(title, content):
        try:
            new_note=Note(title=title, content=content)
            db.session.add(new_note)
            db.session.commit()
            return new_note
        except Exception as e:
            print(e)
            db.session.rollback()
            flash('Invalid Data', "error")
            return False