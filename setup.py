from setuptools import find_packages,setup
def get_requirements(path):
    #this function will return list of requirements
    requirements=[]
    with open(path) as file_obj:
      requirements=file_obj.readlines()
      requirements=[req.replace('\n','') for req in requirements]

      if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements
setup(name='mlproject',version='0.0.1',author='Manish',author_email='manish21169@iiitd.ac.in',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt'))