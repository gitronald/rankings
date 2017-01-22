from setuptools import setup

with open('README.rst') as readme:
  long_description = readme.read()

setup(name='rankings',
      packages=['rankings'],
      version = '0.0.1',
      description = 'Measures for comparing ranked lists',
      long_description = long_description,
      author = 'Ronald E Robertson',
      author_email = 'robertson.ron@husky.neu.edu',
      url = 'https://github.com/gitronald/rankings',
      download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', 
      license='MIT',
      classifiers = ["Intended Audience :: Developers",
                     "Programming Language :: Python :: 2.7",
                     "License :: BSD License"],
      zip_safe=False,
      keywords = ['rankings', 'edit distance', 'jaccard', 'damerau']
      )

