import views
import path_config


route_list = [
	{
		'method': 'GET',
		'path': '/',
		'view': views.index
	},
	{
		'method': 'GET',
		'path': '/showcase',
		'view': views.showcase
	},
	{
		'method': 'GET',
		'path': '/blog',
		'view': views.blog
	},
	{
		'method': 'GET',
		'path': '/about',
		'view': views.about
	}
	,
	{
		'method': 'GET',
		'path': '/post/{name}',
		'view': views.post
	}
]

static_list = [
	{
		'prefix': '/static',
		'path': path_config.STATIC
	},
	{
		'prefix': '/downloads',
		'path': path_config.STATIC + 'downloads/'
	},
	{
		'prefix': '/css',
		'path': path_config.STATIC + 'css/'
	},
	{
		'prefix': '/js',
		'path': path_config.STATIC + 'js/'
	},
	{
		'prefix': '/images',
		'path': path_config.STATIC + 'images/'
	}
]

single_resource_list = [
	{
		'method': 'GET',
		'path': '/favicon.ico',
		'target': 'static/favicon.ico'
	}
]