# flask_sqlalchemy/schema.py
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Brand as BrandModel, Category as CategoryModel, Platform as PlatformModel, Product as ProductModel
from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet

class Brand(SQLAlchemyObjectType):
    class Meta:
        model = BrandModel
        interfaces = (relay.Node, )

class BrandConnection(relay.Connection):
    class Meta:
        node = Brand

class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel
        interfaces = (relay.Node, )

class CategoryConnection(relay.Connection):
    class Meta:
        node = Category

class Platform(SQLAlchemyObjectType):
    class Meta:
        model = PlatformModel
        interfaces = (relay.Node, )

class PlatformConnection(relay.Connection):
    class Meta:
        node = Platform

class Product(SQLAlchemyObjectType):
    class Meta:
        model = ProductModel
        interfaces = (relay.Node, )

class ProductConnection(relay.Connection):
    class Meta:
        node = Product

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Disable sorting over this field
    all_Brand = SQLAlchemyConnectionField(BrandConnection)
    all_Category = SQLAlchemyConnectionField(CategoryConnection)
    all_Platform = SQLAlchemyConnectionField(PlatformConnection)
    all_Product = SQLAlchemyConnectionField(ProductConnection, category_name=graphene.String())


schema = graphene.Schema(query=Query)