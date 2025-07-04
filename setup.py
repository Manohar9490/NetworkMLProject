from setuptools import find_packages, setup
from typing import List


requirement_lst:List[str] =  []
def get_requirements()->List:
  '''
  This function will return list of requirements
  '''
  try:
    with open('requirements.txt','r') as file:
      lines = file.readlines()
      for line in lines:
        requirement = line.strip()
        if requirement and requirement!='-e .':
          requirement_lst.append(requirement)

  except:
    print("file not found")
  
  return requirement_lst


# print(get_requirements())

setup(
  name="NetworkSecurity",
  version='0.0.1',
  author='Manohar',
  author_email= 'manoharkillamsetti@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements()
)