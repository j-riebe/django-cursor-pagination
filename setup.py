from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='mongoengine-cursor-pagination',
    py_modules=['cursor_pagination'],
    version='0.1.5',
    description='Cursor based pagination for Django (Mongoengine-Fork)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Photocrowd',
    author_email='devteam@photocrowd.com',
    url='https://github.com/photocrowd/django-cursor-pagination',
    license='BSD',
    install_requires=["mongoengine"],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Mongoengine',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
