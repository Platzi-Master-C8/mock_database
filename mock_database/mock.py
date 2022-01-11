from mock_database.generators import enum, value, model, phrase, company_name, text, sequence, random_int, name, \
    random_float, url
from mock_database.model import Company, Skill

position_title = phrase(
    enum(['Senior', "Junior"]),
    enum(['Backend', "Frontend", "Go", "Rust", "React", "FullStack", "Machine Learning", "Data Scientist"]),
    value("Developer")
)

skills = ["Python", "Java", "Kotlin", "React", "Angular", "Go", "TensorFlow", "Spring"]
companies = 50

Skills = model(Skill, Skill.id_skill, {
    Skill.skill: sequence(skills)
}, len(skills))

Companies = model(Company, Company.id_company, {
    Company.name: company_name(50),
    Company.description: text(150),
    Company.company_size: random_int(10, 3000),
    Company.ceo: name(50),
    Company.avg_reputation: random_float(0, 100),
    Company.total_ratings: random_int(0, 50),
    Company.ceo_score: random_float(0, 100),
    Company.website: url(),
    Company.culture_score: random_float(0, 100),
    Company.work_life_balance: random_float(0, 100),
    Company.stress_level: random_float(0, 100),
}, companies)


def mock_data():
    Skills()
    Companies()
