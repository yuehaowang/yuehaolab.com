import asyncio
from aiohttp import web
import aiohttp_jinja2


@aiohttp_jinja2.template('index.html')
async def index(request):
	return {'page_title': 'Home'}

@aiohttp_jinja2.template('blog.html')
async def blog(request):
	return {
		'page_title': 'Blog',
		'banner_icon': 'bookmark',
		'banner_subtitle': 'Think, Explore, Create and Share.'
	}

@aiohttp_jinja2.template('showcase.html')
async def showcase(request):
	return {
		'page_title': 'Showcase',
		'banner_icon': 'star',
		'banner_subtitle': 'Discover my projects: frameworks, games and apps.'
	}

@aiohttp_jinja2.template('about.html')
async def about(request):
	return {
		'page_title': 'About',
		'banner_icon': 'user',
		'banner_subtitle': 'Who am I ? Where did I come from ? Where am I going ?'
	}

def view_factory(target):
	async def static_view(request):
		return web.FileResponse(target)

	return static_view
