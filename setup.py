from setuptools import find_packages,setup

hyphen_e = '-e .'

def get_requirements(file_path):
    with open(file=file_path,mode='r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
    return requirements

setup(
    name='Ml project',
    version='0.0.1',
    author='Ankur',
    author_email='cankur728@gmail.com',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=get_requirements('requirements.txt')
)


