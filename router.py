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

resource_list = [
	'/favicon.ico'
]
