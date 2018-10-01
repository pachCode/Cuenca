import sqlalchemy

from sqlalchemy import Column,Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Solution(Base):
    __tablename__ = 'solutions'
    id = Column(Integer, primary_key = True, autoincrement = True)
    queenNumber = Column(Integer)
    solution = Column(Integer)

from sqlalchemy import create_engine
engine = create_engine('sqlite:///solution.sqlite')
from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)

def get_solutions_number(quenNumber):
    s = session()
    return int(s.query(Solution).count()/quenNumber)

def add_solution(solution=[]):
    s = session()
    result = ""
    for i in range(len(solution)):    
        sol = Solution(queenNumber = i+1,solution= solution[i])
        result = result + " ("+ str(i) + ","+str(solution[i])+ ")"
        s.add(sol)
    s.commit()   
    print(result)

def romove_results():
    s = session()
    print(s.query(Solution).count())
    # for user in s.query(Solution):
    #     print(user.solution)
    s.query(Solution).delete()
    s.commit()
    print(s.query(Solution).count())


