"""
    Create our database and fill it with the team
"""
from app import DB
from app.models.teams import Team
from app.models.session import Session
from app.config import (NUMBER_OF_TEAMS, DEFAULT_PASSWORD, DEFAULT_BALANCE,
                        WHITETEAM_USERNAME, WHITETEAM_PASSWORD,
                        REDTEAM_USERNAME, REDTEAM_PASSWORD, TEAM_PRIVATE_KEYS,
                        TEAM_PUBLIC_KEYS)
DB.create_all()

print "Adding teams..."

# ADD WHITE TEAM ACCOUNT
white_team = Team(uuid=1337, username=WHITETEAM_USERNAME,
                  password=WHITETEAM_PASSWORD, balance=1000000000,
                  pub_key=None, private_key=None)

white_team_session = Session(uuid=1337)

DB.session.add(white_team)
DB.session.add(white_team_session)

# ADD RED TEAM ACCOUNT
new_team = Team(uuid=99, username=REDTEAM_USERNAME,
                password=REDTEAM_PASSWORD, balance=0,
                pub_key=None, private_key=None)

new_session = Session(uuid=99)

DB.session.add(new_team)
DB.session.add(new_session)

# add team accounts
for team in range(1, NUMBER_OF_TEAMS+1):

    new_team = Team(uuid=team, username='team{}'.format(team),
                    password=DEFAULT_PASSWORD, balance=DEFAULT_BALANCE,
                    pub_key=TEAM_PUBLIC_KEYS[team], 
                    private_key=TEAM_PRIVATE_KEYS[team])

    new_session = Session(uuid=team)

    DB.session.add(new_team)
    DB.session.add(new_session)

DB.session.commit()
