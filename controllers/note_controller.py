from flask import flash
from models import db
from models.note import Note

class NoteController:
    @staticmethod
    def list_note(page_number=1, per_page=10):
        try:
            notes = Note.query.order_by(Note.id.desc()).paginate(page=page_number, per_page=per_page)
            return notes  # Pagination object
        except Exception as e:
            print("Error in list_note:", e)
            return None

    @staticmethod
    def create_note(title, content):
        try:
            new_note = Note(title=title, content=content)
            db.session.add(new_note)
            db.session.commit()
            return new_note
        except Exception as e:
            print("Error in create_note:", e)
            db.session.rollback()
            flash('Invalid Data', "error")
            return False

    @staticmethod
    def get_recent_notes(limit=3):
        """Return a simple list of the most recent notes"""
        try:
            return Note.query.order_by(Note.id.desc()).limit(limit).all()
        except Exception as e:
            print("Error in get_recent_notes:", e)
            return []
