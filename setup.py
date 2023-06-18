from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)-> List[str]:
    """
    This function returns a list of requirements
    
    """
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            






setup(
name  = 'scm',
version = '0.0.1',    
author = 'chandan D. Chaudhari',
author_email = 'chaudhari.chandan22@gmail.com',
packages = find_packages(),
install_requires = ['pandas','numpy','seaborn']    
    
    
    
    
    
    
    
)