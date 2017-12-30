import asyncio
from aiohttp import web
import aiohttp_jinja2


@aiohttp_jinja2.template('index.html')
async def index(request):
	return {'subtitle': 'Home'}

@aiohttp_jinja2.template('blog.html')
async def blog(request):
	return {'subtitle': 'Blog'}

@aiohttp_jinja2.template('showcase.html')
async def showcase(request):
	return {'subtitle': 'Showcase'}

@aiohttp_jinja2.template('about.html')
async def about(request):
	return {'subtitle': 'About'}
