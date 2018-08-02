import asyncio
from aiohttp import web
import aiohttp_jinja2
import json
import time
import markdown


REFRESH_BLOG_PERIOD = 60;


class PostUtils:
	post_list = {}

	__pre_load_time = -1

	def load_post_list():
		curr_time = time.time()

		if PostUtils.__pre_load_time > 0 and curr_time - PostUtils.__pre_load_time < REFRESH_BLOG_PERIOD:
			return

		PostUtils.__pre_load_time = curr_time

		with open('static/posts/list.json', 'r', encoding='utf8') as f:
			PostUtils.post_list = json.loads(f.read())


@aiohttp_jinja2.template('index.html')
async def index(request):
	return {'page_title': 'Home'}

@aiohttp_jinja2.template('blog.html')
async def blog(request):
	PostUtils.load_post_list()

	return {
		'page_title': 'Blog',
		'banner_icon': 'bookmark',
		'banner_subtitle': 'Think, Explore, Create and Share.',
		'post_list': PostUtils.post_list
	}

@aiohttp_jinja2.template('post.html')
async def post(request):
	PostUtils.load_post_list()

	post_name = request.match_info['name']

	if post_name in PostUtils.post_list:
		post = PostUtils.post_list[post_name]

		post_title = post["title"]
		post_time = post["date"]

		with open('static/posts/%s.md' % post_name, 'r', encoding='utf8') as f:
			html = markdown.markdown(f.read())
	else:
		post_title = "404 Not Found"
		post_time = ""

		html = '<h1>Oops, cannot find the post :(</h1>'
	
	return {
		'page_title': post_title,
		'post_time': post_time,
		'post_content': html
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
