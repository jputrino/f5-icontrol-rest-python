#!/usr/bin/env python

# Copyright 2015 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from setuptools import setup

import icontrol


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='f5-icontrol-rest',
      description='F5 BIG-IP iControl REST API client',
      long_description=readme(),
      license='Apache License, Version 2.0',
      version=icontrol.__version__,
      author='F5 Networks',
      author_email='f5-icontrol-rest-python@f5.com',
      url='https://github.com/F5Networks/f5-icontrol-rest-python',
      install_requires=[
          'requests',
      ],
      py_modules=[
          'icontrol.session',
      ],
      packages=['icontrol'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Intended Audience :: System Administrators',
      ]
      )
