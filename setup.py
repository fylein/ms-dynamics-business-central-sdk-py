import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='ms-dynamics-business-central-sdk',
    version='1.4.1',
    author='Shwetabh Kumar',
    author_email='shwetabh.kumar@fyle.in',
    description='Python SDK for accessing Dynamics APIs',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',  
    keywords=['dynamics', 'business-central', 'ms', 'ms-dynamics-business-central', 'fyle', 'api', 'python', 'sdk'],
    url='https://github.com/fylein/ms-dynamics-business-central-sdk-py',
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
