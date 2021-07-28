from fastapi import APIRouter

from models.blog import Blog
from config.db import conn
from schemas.blog import blogEntity,blogsEntity
from bson import ObjectId


blog = APIRouter()

@blog.get('/')
async def find_all_blogs():
    print (conn.local.blog.find())
    print (blogsEntity(conn.local.blog.find()))
    return blogsEntity(conn.local.blog.find())


@blog.post('/')
async def create_blog(blog: Blog):
    conn.local.blog.insert_one(dict(blog))
    return blogsEntity(conn.local.blog.find())


@blog.get('/{id}')
async def find_one_blog(id):
    return blogEntity(conn.local.blog.find_one({"_id":ObjectId(id)}))   