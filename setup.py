from setuptools import setup, find_packages


install_requires = [
  'flask == 0.10.1', 'flask-script == 2.0.5', 'sqlalchemy == 0.9.8',
  'alembic == 0.7.4', 'itsdangerous == 0.24', 'bcrypt == 1.1.0', 'Flask-SQLAlchemy == 1.0'
]

test_require = [
    'pytest == 2.6.4',
]

docs_require = [
    'sphinx == 1.2.3',
]

setup(
    name='simple_python_project',
    version='0.0.1',
    author='jihyun',
    author_email='noblea1117@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=test_require,
    extras_require={
        'docs': docs_require,
        'tests': test_require
    }
)