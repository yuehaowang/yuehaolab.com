import sys
import os
import logging
from datetime import datetime
from aiohttp import web
import jinja2
import aiohttp_jinja2

import router
import path_config
import views


def create_web_server(port):
	app = web.Application()

	# jinja2 setup
	aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(path_config.TEMPLATES))

	# add url routers
	for route in router.route_list:
		app.router.add_route(route['method'], route['path'], route['view'])

	for static in router.static_list:
		app.router.add_static(static['prefix'], static['path'])

	for single_res in router.single_resource_list:
		app.router.add_route(single_res['method'], single_res['path'], views.view_factory(single_res['target']))

	# run the server on a specified port
	web.run_app(app, port=port)


if __name__ == '__main__':
	try:
		# make 'logs' directory if it doesn't exist
		os.makedirs(path_config.LOGS, exist_ok=True)
		# create the PY_SERVER_LOG file if it doesn't exist
		if not os.path.exists(path_config.PY_SERVER_LOG):
			f = open(path_config.PY_SERVER_LOG, 'w')
			f.close()

		# configure logging
		logging.basicConfig(filename=path_config.PY_SERVER_LOG, level=logging.INFO)

		logging.info('Start on %s' % datetime.now())

		# get the port where the server works
		if len(sys.argv) >= 2:
			port = int(sys.argv[1])
		else:
			port = 9331

		# start the server
		create_web_server(port)

	finally:
		logging.info('Exit on %s' % datetime.now())
