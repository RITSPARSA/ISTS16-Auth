"""
    Create our database and fill it with the team
"""
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from app import DB
from app.models.teams import Team
from app.models.session import Session
from app.config import (TEAMS, DEFAULT_PASSWORD, DEFAULT_BALANCE,
                        WHITETEAM_USERNAME, WHITETEAM_PASSWORD,
                        REDTEAM_USERNAME, REDTEAM_PASSWORD)
DB.create_all()

print "Adding teams..."

# ADD WHITE TEAM ACCOUNT
new_team = Team(uuid=0, username=WHITETEAM_USERNAME,
                password=WHITETEAM_PASSWORD, balance=1000000000,
                pub_key=None, private_key=None)

new_session = Session(uuid=0)

DB.session.add(new_team)
DB.session.add(new_session)

# ADD RED TEAM ACCOUNT
new_team = Team(uuid=99, username=REDTEAM_USERNAME,
                password=REDTEAM_PASSWORD, balance=0,
                pub_key=None, private_key=None)

new_session = Session(uuid=99)

DB.session.add(new_team)
DB.session.add(new_session)

# add team accounts
for team in TEAMS:
    key = rsa.generate_private_key(
        backend=default_backend(),
        public_exponent=65537,
        key_size=2048
    )
    private_key = key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption())

    public_key = key.public_key().public_bytes(
        serialization.Encoding.OpenSSH,
        serialization.PublicFormat.OpenSSH
    )

    new_team = Team(uuid=team, username='team{}'.format(team),
                    password=DEFAULT_PASSWORD, balance=DEFAULT_BALANCE,
                    pub_key=public_key, private_key=private_key)

    new_session = Session(uuid=team)

    DB.session.add(new_team)
    DB.session.add(new_session)

DB.session.commit()
