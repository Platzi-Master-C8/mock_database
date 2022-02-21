import datetime
from mock_database.generators import enum, value, model, phrase, company_name, text, sequence, random_int, name, \
    random_float, url, boolean, datetime_between
from mock_database.model import (
    Company,
    Skill,
    Perk,
    CompanyPerk,
    Location,
    CompanyLocation,
    Seniority,
    Currency,
    PositionCategory,
    Position,
    PositionSkill,
    UserReview
)


def mock_data():
    position_title = phrase(
        enum(['Senior', "Junior"]),
        enum(['Backend', "Frontend", "Go", "Rust", "React", "FullStack", "Machine Learning", "Data Scientist"]),
        value("Developer")
    )
    modality = enum(["remote", "office", "hybrid"])

    skills = ["Python", "Java", "Kotlin", "React", "Angular", "Go", "TensorFlow", "Spring", "Quarkus", "Micronaut",
              "Rust", "Svelte", "Clojure", "FastAPI", "pandas", "numpy"]
    seniority = ["Junior Engineer", "Senior Engineer", "Lead Engineer", "Principal Engineer", "Staff Engineer"]
    perks = ["Remote work", "Snacks", "BYOD", "Day Off", "Prepaid medicine"]
    currency = ["USD"]
    currency_country = ["United States"]
    position_category = ["Developer", "Ux/Ui", "Testing", "Product Manager", "Project Manager", "Datascientist",
                         "Machine Learning engineer"]
    companies = 50
    positions = 100

    Skills = model(Skill, Skill.id_skill, {
        Skill.skill: sequence(skills)
    }, len(skills))

    Seniorities = model(Seniority, Seniority.id_seniority, {
        Seniority.seniority: sequence(seniority)
    }, len(seniority))

    Currencies = model(Currency, Currency.id_currency, {
        Currency.currency: sequence(currency),
        Currency.country: sequence(currency_country)
    }, len(currency))

    PositionCategories = model(PositionCategory, PositionCategory.id_position_category, {
        PositionCategory.category: sequence(position_category)
    }, len(position_category))

    Perks = model(Perk, Perk.id_perk, {
        Perk.perk: sequence(perks)
    }, len(perks))

    Companies = model(Company, Company.id_company, {
        Company.name: company_name(50),
        Company.description: text(150),
        Company.company_premium: boolean(),
        Company.company_size: random_int(10, 3000),
        Company.ceo: name(50),
        Company.avg_reputation: random_float(0, 100),
        Company.total_ratings: random_int(0, 50),
        Company.ceo_score: random_float(0, 100),
        Company.website: url(),
        Company.culture_score: random_float(0, 100),
        Company.work_life_balance: random_float(0, 100),
        Company.stress_level: random_float(0, 100),
        Company.carrer_opportunities: random_float(0, 100)
    }, companies)

    CompanyPerks = model(CompanyPerk, CompanyPerk.id_company_perk, {
        CompanyPerk.perk_id: Perks.id(),
        CompanyPerk.company_id: Companies.id(True)
    }, companies)

    Locations = model(Location, Location.id_location, {
        Location.country: enum(["Colombia", "Mexico", "Canada", "Estados Unidos"]),
        Location.continent: value("America")
    }, companies)

    CompanyLocations = model(CompanyLocation, CompanyLocation.id_company_location, {
        CompanyLocation.company_id: Companies.id(True),
        CompanyLocation.location_id: Locations.id(True)
    }, companies)

    Positions = model(Position, Position.id_position, {
        Position.position_title: position_title,
        Position.position_category_id: PositionCategories.id(),
        Position.seniority_id: Seniorities.id(),
        Position.description: text(300),
        Position.modality: modality,
        Position.date_position: datetime_between(datetime.datetime(2021, 1, 1), datetime.datetime(2022, 1, 31)),
        Position.activate: boolean(),
        Position.num_offers: random_int(1, 10),
        Position.salary_min: random_int(1000, 2000),
        Position.salary_max: random_int(2000, 9000),
        Position.salary: random_int(1000, 9000),
        Position.currency_id: Currencies.id(),
        Position.remote: boolean(),
        Position.location_id: Locations.id(),
        Position.english: boolean(),
        Position.english_level: enum(["A2", "B1", "B2", "C1", "C2"]),
        Position.position_url: url(),
        Position.company_id: Companies.id(),
        Position.uid: text(300)
    }, positions)

    PositionSkills = model(PositionSkill, PositionSkill.id_position_skill, {
        PositionSkill.skill_id: Skills.id(),
        PositionSkill.position_id: Positions.id(True)
    }, positions * 5)

    UserReviews = model(UserReview, UserReview.id_review, {
        UserReview.company_id: Companies.id(),
        UserReview.review_title: text(150),
        UserReview.job_location: text(150),
        UserReview.is_still_working_here: boolean(),
        UserReview.position_user: position_title,
        UserReview.content_type: text(300),
        UserReview.review_score: random_float(0, 100),
        UserReview.review_date: datetime_between(datetime.datetime(2019, 1, 1), datetime.datetime(2020, 12, 31)),
        UserReview.utility_counter: random_int(0, 300),
        UserReview.score_work_environment: random_float(0, 100),
        UserReview.score_career_development: random_float(0, 100),
        UserReview.score_culture: random_float(0, 100),
        UserReview.score_perks: random_float(0, 100),
        UserReview.score_stress_level: random_float(0, 100),
        UserReview.score_work_life_balance: random_float(0, 100),
        UserReview.diversity_score: random_float(0, 100),
        UserReview.review_link: url()
    }, positions * 10)

    Skills()
    Seniorities()
    Currencies()
    PositionCategories()
    Positions()
    PositionSkills()
    Perks()
    Locations()
    Companies()
    CompanyPerks()
    CompanyLocations()
    UserReviews()
