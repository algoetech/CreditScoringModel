from faker import Faker 
from faker_credit_score import CreditScore

fake = Faker()
fake.add_provider(CreditScore)

fake.credit_score_name()
# 'TransUnion FICO Risk Score, Classic 04'
fake.credit_score_provider()
# 'TransUnion'
fake.credit_score()
# 791