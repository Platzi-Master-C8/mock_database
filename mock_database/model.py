from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Skill(Base):
    __tablename__ = 'skill'

    id_skill = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    skill = Column(String(150), nullable=False)
    skill_position = relationship('Position', secondary='position_skill')


class Seniority(Base):
    __tablename__ = 'seniority'

    id_seniority = Column(Integer, primary_key=True, autoincrement=True)
    seniority = Column(String(50), nullable=False)


class Currency(Base):
    __tablename__ = 'currency'

    id_currency = Column(Integer, primary_key=True, autoincrement=True)
    currency = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)


class PositionCategory(Base):
    __tablename__ = 'position_category'

    id_position_category = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(50), nullable=False)


class Position(Base):
    __tablename__ = 'position'

    id_position = Column(Integer, primary_key=True, autoincrement=True)
    position_title = Column(String(150), nullable=False)
    position_category_id = Column(Integer, ForeignKey('position_category.id_position_category'))
    position_category = relationship('PositionCategory')
    seniority_id = Column(Integer, ForeignKey('seniority.id_seniority'))
    seniority = relationship('Seniority')
    description = Column(Text, nullable=False)
    modality = Column(String(50), nullable=False)
    date_position = Column(DateTime, nullable=False)
    activate = Column(Boolean, default=True, nullable=False)
    num_offers = Column(Integer, default=1, nullable=True)
    salary_min = Column(Integer, nullable=True)
    salary_max = Column(Integer, nullable=True)
    salary = Column(Integer, nullable=True)
    currency_id = Column(Integer, ForeignKey('currency.id_currency'))
    currency = relationship('Currency')
    remote = Column(Boolean, nullable=False)
    location_id = Column(Integer, ForeignKey('location.id_location'))
    position_location = relationship('Location')
    english = Column(Boolean, nullable=False)
    english_level = Column(String(50), nullable=True)
    position_url = Column(Text, nullable=False)
    company_id = Column(Integer, ForeignKey('company.id_company'))
    position_company = relationship('Company')
    position_skill = relationship('Skill', secondary='position_skill')


class PositionSkill(Base):
    __tablename__ = 'position_skill'

    id_position_skill = Column(Integer, primary_key=True, autoincrement=True)
    position_id = Column(Integer, ForeignKey('position.id_position'))
    skill_id = Column(Integer, ForeignKey('skill.id_skill'))


class CompanyPerk(Base):
    __tablename__ = 'company_perk'

    id_position_perk = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('company.id_company'))
    perk_id = Column(Integer, ForeignKey('perk.id_perk'))


class Perk(Base):
    __tablename__ = 'perk'

    id_perk = Column(Integer, primary_key=True, autoincrement=True)
    perk = Column(String(150), nullable=False)
    perk_company = relationship('Company', secondary='company_perk')


class Company(Base):
    __tablename__ = 'company'

    id_company = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    company_premium = Column(Boolean, default=False)
    company_size = Column(Integer, nullable=True)
    ceo = Column(String(50), nullable=False)
    avg_reputation = Column(Float, nullable=True)
    total_ratings = Column(Integer, nullable=True)
    ceo_score = Column(Float, nullable=True)
    website = Column(String(150), nullable=True)
    culture_score = Column(Float, nullable=True)
    work_life_balance = Column(Float, nullable=True)
    stress_level = Column(Float, nullable=True)
    company_location = relationship('Location', secondary='company_location')
    company_perk = relationship('Perk', secondary='company_perk')


class CompanyLocation(Base):
    __tablename__ = 'company_location'

    id_company_location = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('company.id_company'))
    location_id = Column(Integer, ForeignKey('location.id_location'))


class Location(Base):
    __tablename__ = 'location'

    id_location = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(50), nullable=False)
    continent = Column(String(50), nullable=False)
    location_company = relationship('Company', secondary='company_location')


class UserReview(Base):
    __tablename__ = 'user_review'

    id_review = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('company.id_company'))
    review_company = relationship('Company')
    title = Column(String(150), nullable=True)
    position_user = Column(String(50), nullable=True)
    pros = Column(Text, nullable=True)
    const = Column(Text, nullable=True)
    review_score = Column(Float, nullable=False)
    review_date = Column(DateTime, nullable=False)
    useful = Column(Integer, nullable=True)
    score_culture = Column(Float, nullable=True)
    score_perks = Column(Float, nullable=True)
    score_work = Column(Float, nullable=True)
    score_stress_level = Column(Float, nullable=True)
    score_work_life_balance = Column(Float, nullable=True)
    review_link = Column(Text, nullable=False)


class UserInterview(Base):
    __tablename__ = 'user_interview'

    id_review = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('company.id_company'))
    interview_company = relationship('Company')
    title = Column(String(150), nullable=True)
    job_position = Column(String(50), nullable=True)
    difficult = Column(Float, nullable=True)
    description = Column(Text, nullable=False)
    interview_date = Column(DateTime, nullable=True)
    interview_link = Column(Text, nullable=False)
