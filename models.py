from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    victories = Column(Integer)
    championships = Column(Integer)

    drivers = relationship("Driver", back_populates="team")


class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    team_name_id = Column(Integer, ForeignKey("teams.id"))
    first_name = Column(String, nullable=False, unique=True)
    last_name = Column(String, nullable=False, unique=True)
    number = Column(Integer, unique=True)
    age = Column(Integer, nullable=False)
    nationality = Column(String)

    team = relationship("Team", back_populates="drivers")


class Circuit(Base):
    __tablename__ = "circuits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    length = Column(Float)
    laps = Column(Integer)
    lap_record = Column(Integer)
    race_distance = Column(Float)
    num_corners = Column(Integer)


class DriverRank(Base):
    __tablename__ = "driver_rank"

    id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(Integer, ForeignKey("drivers.id"))
    team_id = Column(Integer, ForeignKey("teams.id"))
    points = Column(Integer)
    position = Column(Integer)

    driver = relationship("Driver")
    team = relationship("Team")


class TeamRank(Base):
    __tablename__ = "team_rank"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    points = Column(Integer)
    position = Column(Integer)

    team = relationship("Team")
