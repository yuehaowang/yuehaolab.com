#!/usr/bin/env python3


import sys
import os
import logging
import argparse
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
		try:
			app.router.add_route(route['method'], route['path'], route['view'])
		except ValueError as e:
			print('WARNING: %s' % e)


	# the code below is just used for loading static resource when testing locally
	for static in router.static_list:
		try:
			app.router.add_static(static['prefix'], static['path'])
		except ValueError as e:
			print('WARNING: %s' % e)

	for single_res in router.single_resource_list:
		try:
			app.router.add_route(single_res['method'], single_res['path'], views.view_factory(single_res['target']))
		except ValueError as e:
			print('WARNING: %s' % e)

	# run the server on a specified port
	web.run_app(app, port=port)


parser = argparse.ArgumentParser(description='The python server that works on yuehaolab.com.')
parser.add_argument('--logfile', help='Path to the log file.', default='', type=str)
parser.add_argument('--port', help='The port where the server works.', default=9331, type=int)

if __name__ == '__main__':
	try:
		args = parser.parse_args()

		# configure logging
		if args.logfile != '' and os.path.exists(args.logfile):
			logging.basicConfig(filename=args.logfile, level=logging.INFO)	

		logging.info('Start on %s' % datetime.now())

		# start the server
		create_web_server(args.port)

	finally:
		logging.info('Exit on %s' % datetime.now())
