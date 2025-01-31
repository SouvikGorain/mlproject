from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .' # whenever we are trying to install all the requirements.txt, setup.py file should run to build the packages
def get_requirements(file_path:str)->List[str]:  #to enable that we specifically write '-e .' in requirements to automatically trigger/connect to setup.py 
    '''                                          
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj: # create a file object with the contents present in file path
        requirements=file_obj.readlines() # read each requirements line by line but \n will also get recorded and we need to replace it with blank space
        requirements=[req.replace("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
name = 'mlproject',
version='0.0.1',
author = 'souvik',
author_email='souvikgorain02@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')        #['pandas','numpy','seaborn']

)

#python config file is mainly to tell AWS elastic beanstalk what is the entry point of your application