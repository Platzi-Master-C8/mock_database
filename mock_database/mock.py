from mock_database.generators import enum, value, model, phrase, company_name, text, sequence, random_int, name, \
    random_float, url, boolean
from mock_database.model import Company, Skill, Perk, CompanyPerk, Location, CompanyLocation

position_title = phrase(
    enum(['Senior', "Junior"]),
    enum(['Backend', "Frontend", "Go", "Rust", "React", "FullStack", "Machine Learning", "Data Scientist"]),
    value("Developer")
)

skills = ["Python", "Java", "Kotlin", "React", "Angular", "Go", "TensorFlow", "Spring"]
perks = ["Remote work", "Snacks", "BYOD", "Day Off", "Prepaid medicine"]
companies = 50

Skills = model(Skill, Skill.id_skill, {
    Skill.skill: sequence(skills)
}, len(skills))

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
    Company.stress_level: random_float(0, 100)
}, companies)

CompanyPerks = model(CompanyPerk, CompanyPerk.id_position_perk, {
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


def mock_data():
    Skills()
    Perks()
    Locations()
    Companies()
    CompanyPerks()
    CompanyLocations()
