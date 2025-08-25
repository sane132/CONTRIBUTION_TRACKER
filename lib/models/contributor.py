from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, validates
from .base import Base, session
from .contribution import Contribution

class Contributor(Base):
    """Represents a contributor (member, volunteer, or donor)."""
    __tablename__ = 'contributors'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    contact_info = Column(String)
    type = Column(String)  # member, volunteer, or donor
    target_amount = Column(Float, default=0.0)
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    
    # Relationships
    organization = relationship("Organization", back_populates="contributors")
    contributions = relationship("Contribution", back_populates="contributor", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Contributor(id={self.id}, name='{self.first_name} {self.last_name}', type='{self.type}')>"
    
    # Property for full name
    @property
    def full_name(self):
        """Returns the full name of the contributor."""
        return f"{self.first_name} {self.last_name}"
    
    # Property to calculate actual contributions total
    @property
    def total_contributions(self):
        """Calculates the total amount contributed by this contributor."""
        # Use session to query for contributions directly
        from .contribution import Contribution
        contributions = session.query(Contribution).filter(Contribution.contributor_id == self.id).all()
        return sum(contribution.amount for contribution in contributions)
    
    # Property to calculate remaining amount
    @property
    def remaining_amount(self):
        """Calculates the remaining amount needed to reach the target."""
        return max(0, self.target_amount - self.total_contributions)
    
    # Property to calculate progress percentage
    @property
    def progress_percentage(self):
        """Calculates the percentage of the target reached."""
        if self.target_amount == 0:
            return 0
        return (self.total_contributions / self.target_amount) * 100
    
    # Validation
    @validates('type')
    def validate_type(self, key, type):
        """Validates that the type is one of the allowed values."""
        if type not in ['member', 'volunteer', 'donor']:
            raise ValueError("Type must be 'member', 'volunteer', or 'donor'")
        return type
    
    @validates('target_amount')
    def validate_target_amount(self, key, target_amount):
        """Validates that the target amount is not negative."""
        if target_amount < 0:
            raise ValueError("Target amount cannot be negative")
        return target_amount
    
    # ORM methods
    @classmethod
    def create(cls, first_name, last_name, contact_info, type, organization_id, target_amount=0.0):
        """Creates a new contributor."""
        contributor = cls(
            first_name=first_name, 
            last_name=last_name, 
            contact_info=contact_info, 
            type=type, 
            target_amount=target_amount,
            organization_id=organization_id
        )
        session.add(contributor)
        session.commit()
        return contributor
    
    @classmethod
    def update_target_amount(cls, contributor_id, target_amount):
        """Updates the target contribution amount for a contributor."""
        contributor = cls.find_by_id(contributor_id)
        if contributor:
            contributor.target_amount = target_amount
            session.commit()
            return True
        return False
    
    @classmethod
    def get_all(cls):
        """Returns all contributors."""
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        """Finds a contributor by their ID."""
        return session.query(cls).filter(cls.id == id).first()
    
    @classmethod
    def find_by_name(cls, first_name, last_name):
        """Finds a contributor by their full name."""
        return session.query(cls).filter(
            cls.first_name == first_name, 
            cls.last_name == last_name
        ).first()
    
    @classmethod
    def find_by_type(cls, type):
        """Finds all contributors of a specific type."""
        return session.query(cls).filter(cls.type == type).all()
    
    @classmethod
    def delete(cls, id):
        """Deletes a contributor by their ID."""
        contributor = cls.find_by_id(id)
        if contributor:
            session.delete(contributor)
            session.commit()
            return True
        return False