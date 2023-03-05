from setuptools import find_packages,setup
from typing import List

hyphen_dot = '-e .'

def get_requirements(file_path:str) -> List[str]:

    '''
    This function will recieve path of the requirements.txt file
    and return the lists of packages
    '''

    requirements = []

    with open('requirements.txt') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]

    if hyphen_dot in requirements: requirements.remove(hyphen_dot)
        
    
    return requirements

setup(
name='end_to_end_ml',
version='0.0.1',
author='Michael Tamirie',
author_email='michaeltamirie@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)