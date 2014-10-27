from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='document_identifier',
      version='0.1',
      description='Attempts to identify machine readable documents',
      long_description=readme(),
      url='http://github.com/klupamos/Document_Identifier',
      author='Greg Klupar',
      author_email='klupamos+github@gmail.com',
      license='MIT',
      packages=['document_identifier'],
      include_package_data=True,
      zip_safe=False)
