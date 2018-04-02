from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='ena',
        version='0.2',
        description='Ena is an Electronic Neural Assistant designed for use in the terminal or command prompt',
        url='http://github.com/madamson8/ena',
        author='Matthew Adamson, Heber Brau',
        author_email='matthewadamson8@gmail.com',
        license='MIT',
        packages=['ena'],
        install_requires=[
                'passlib==1.7.1',
                'psycopg2==2.7.4',
        ],
        zip_safe=False)
