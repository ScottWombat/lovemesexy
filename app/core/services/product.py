from app.core.db import get_db, db_client
from app.core.models.product import Product
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import json
class ProductService:
    def __init__(self,db: AsyncIOMotorClient):
        self.db  = db
        #print("KKKK")
        #print(self.client)
        #self.product_collection =  client.get_collection("mymongo")
        ...
        
    
    #@classmethod  
    #def get_product(cls):
    #    return cls()
    
    async def create(self,product_data: Product):
        #data = Product(name="dildo")
        #coll = self.db.get_collection("products")
        #db = get_db()
        print("coll")
        p_col = self.db.get_collection("products")
        print(p_col)
        data = {'_id': 123,'name3': 'rev'}
        print("KKKKK1")
        j = product_data.__dict__
        print(j)
        #product = await p_col.insert_one(product_data.__dict__)
        product = await p_col.insert_one(data)
        print(product.inserted_id )
