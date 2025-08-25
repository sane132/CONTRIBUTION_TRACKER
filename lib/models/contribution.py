from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship, validates
from datetime import datetime
from .base import Base, session

class Contribution(Base):
    """Represents a financial contribution."""
    __tablename__ = 'contributions'
    
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, default=datetime.now)
    notes = Column(String)
    contributor_id = Column(Integer, ForeignKey('contributors.id'))
    
    # Relationship
    contributor = relationship("Contributor", back_populates="contributions")
    
    def __repr__(self):
        return f"<Contribution(id={self.id}, amount={self.amount}, date='{self.date}')>"
    
    # Validation
    @validates('amount')
    def validate_amount(self, key, amount):
        """Validates that the contribution amount is positive."""
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return amount
    
    # ORM methods
    @classmethod
    def create(cls, amount, contributor_id, notes=None, date=None):
        """Creates a new contribution."""
        if date is None:
            date = datetime.now()
            
        contribution = cls(
            amount=amount, 
            contributor_id=contributor_id, 
            notes=notes, 
            date=date
        )
        session.add(contribution)
        session.commit()
        return contribution
    
    @classmethod
    def get_all(cls):
        """Returns all contributions."""
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        """Finds a contribution by its ID."""
        return session.query(cls).filter(cls.id == id).first()
    
    @classmethod
    def find_by_contributor(cls, contributor_id):
        """Finds all contributions for a specific contributor."""
        return session.query(cls).filter(cls.contributor_id == contributor_id).all()
    
    @classmethod
    def find_by_date_range(cls, start_date, end_date):
        """Finds contributions within a specific date range."""
        return session.query(cls).filter(
            cls.date >= start_date, 
            cls.date <= end_date
        ).all()
    
    @classmethod
    def delete(cls, id):
        """Deletes a contribution by its ID."""
        contribution = cls.find_by_id(id)
        if contribution:
            session.delete(contribution)
            session.commit()
            return True
        return False