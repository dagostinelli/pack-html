import logging
import click
from . import pack as packcmd
import sys
from datetime import date
import json

copyright_string = '%(prog)s %(version)s Copyright ' + str(date.today().year) + ' Darryl T. Agostinelli. All Rights Reserved.'


def main():
	return pack_html(prog_name="pack-html")


def process_extra(extra):
	try:
		return json.loads(extra)
	except:
		# not json
		return dict()


@click.command()
@click.argument('input', type=click.File('rb'))
@click.option('--root-dir', type=click.Path(writable=False))
@click.option('-o', '--out', type=click.Path(writable=True))
@click.option('--ignore-errors', is_flag=True, default=False)
@click.option('--verbose', envvar='PACK_HTML_VERBOSE', is_flag=True, default=False, help='Show detailed step by step logging')
@click.option('--debug', envvar='PACK_HTML_DEBUG', is_flag=True, default=False, help='Show all kinds of low-level messages')
@click.version_option("1.0", prog_name="pack-html", message=copyright_string)
def pack_html(verbose, debug, input, root_dir, out, ignore_errors):
	"""Given an html file, combine all of the images, css and js into a single file"""

	# basic logging handler is null
	handlers = [
		logging.NullHandler()
	]

	# basic log level
	loglevel = logging.INFO

	# if debug is on, then output the whole thing to the stream
	if debug:
		handlers.append(logging.StreamHandler())
		loglevel = logging.DEBUG

	logging.basicConfig(
		level=loglevel,
		format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
		datefmt='%H:%M:%S',
		handlers=handlers
	)

	code = packcmd.pack(input.name, input.read(), ignore_errors=ignore_errors, root_dir=root_dir)
	if out:
		with open(out, 'w') as out_file:
			out_file.write(code)
	click.echo(code)


if __name__ == "__main__":
	sys.exit(main())
