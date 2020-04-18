# flask_sqlalchemy/models.py
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref, foreign)
from sqlalchemy.ext.declarative import declarative_base

# https://data.heroku.com/datastores/47d28f6a-6d7a-4dbf-ae66-260e941faff9#administration
DBMS = 'postgresql'
USERNAME = '???'
PASSWORD = '???'
HOST = 'ec2-34-204-22-76.compute-1.amazonaws.com'
DATABASE = 'd1rct01jj1tj1v'

database_engine = ''.join([DBMS, '://', USERNAME, ':', PASSWORD, '@', HOST, '/', DATABASE])


engine = create_engine(database_engine, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()

class Brand(Base):
    __tablename__ = 'tb_brand'
    id_brand = Column(Integer, primary_key=True)
    tx_name = Column(String)

class Category(Base):
    __tablename__ = 'tb_category'
    id_category = Column(Integer, primary_key=True)
    tx_name = Column(String)

class Platform(Base):
    __tablename__ = 'tb_platform'
    id_platform = Column(Integer, primary_key=True)
    tx_name = Column(String)

class Product(Base):
    __tablename__ = 'tb_product'
    id_product = Column(Integer, primary_key=True)   
    tx_name = Column(String)      
    tx_description = Column(String) 
    
    cd_category = Column(Integer, ForeignKey('tb_category.id_category'))    
    tx_category = relationship(
        'Category',
        primaryjoin=(cd_category == foreign(Category.id_category)),
        uselist=False,
    )
    
    cd_1st_brand = Column(Integer, ForeignKey('tb_brand.id_brand'))     
    tx_1st_brand = relationship(
        'Brand',
        primaryjoin=(cd_1st_brand == foreign(Brand.id_brand)),
        uselist=False,
    )

    # implement relationship
    cd_2nd_brand = Column(Integer)      
    cd_3rd_brand = Column(Integer)      
    cd_4th_brand = Column(Integer) 

    cd_platform = Column(Integer, ForeignKey('tb_platform.id_platform'))   
    tx_platform = relationship(
        'Platform',
        primaryjoin=(cd_platform == foreign(Platform.id_platform)),
        uselist=False,
    )

    nr_height = Column(Numeric)         
    nr_depth = Column(Numeric)          
    nr_weight = Column(Numeric)   
    nr_paid_price = Column(Numeric)                 
    tx_main_image_url = Column(String) 