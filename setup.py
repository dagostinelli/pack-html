from setuptools import setup

version = open('VERSION').read().strip()

requirements = [
	# put packages here
	'wheel',
	'click',
	'beautifulsoup4',
	'requests',
	'cssutils'
]

setup_options = dict(
	name='pack-html',
	version=version,
	author='Darryl T. Agostinelli',
	author_email='dagostinelli@gmail.com',
	url='https://github.com/dagostinelli/pack-html',
	description='Webpage Packer',
	long_description=open('README.md').read().strip(),
	packages=['pack_html'],
	install_requires=requirements,
	tests_require=requirements,
	test_suite='tests',
	entry_points={
		'console_scripts': [
			'pack-html=pack_html.__main__:main',
		]
	}
)

setup(**setup_options)
