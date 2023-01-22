import setuptools

with open('readme.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='psr.event',
    version='1.0.0',
    description='Standard interfaces for event handling',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='License :: OSI Approved :: MIT License',
    package_dir={'psr': 'lib/psr'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    py_modules=['psr.event'],
    python_requires='>=3.6',
)
