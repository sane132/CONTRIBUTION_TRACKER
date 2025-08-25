from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base, session

class Organization(Base):
    """Represents an organization in the database."""
    __tablename__ = 'organizations'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_info = Column(String)
    
    # One-to-many relationship with contributors
    contributors = relationship("Contributor", back_populates="organization", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Organization(id={self.id}, name='{self.name}')>"
    
    # ORM methods
    @classmethod
    def create(cls, name, contact_info):
        """Creates a new organization."""
        organization = cls(name=name, contact_info=contact_info)
        session.add(organization)
        session.commit()
        return organization
    
    @classmethod
    def get_all(cls):
        """Returns all organizations."""
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        """Finds an organization by its ID."""
        return session.query(cls).filter(cls.id == id).first()
    
    @classmethod
    def delete(cls, id):
        """Deletes an organization by its ID."""
        organization = cls.find_by_id(id)
        if organization:
            session.delete(organization)
            session.commit()
            return True
        return False