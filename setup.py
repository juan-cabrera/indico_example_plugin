# This file is part of the Indico plugins.
# Copyright (C) 2020 UNamur
#
# The Indico plugins are free software; you can redistribute
# them and/or modify them under the terms of the MIT License;
# see the LICENSE file for more details.

from __future__ import unicode_literals

from setuptools import find_packages, setup


setup(
    name='indico-example-plugin',
    version='0.0.1',
    description='Indico plugin example',
    url='https://github.com/juan-cabrera/indico_example_plugin',
    license='MIT',
    author='J Cabrera',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'indico>=2.0'
    ],
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    entry_points={'indico.plugins': {'example_plugin = indico_example_plugin.plugin:ExamplePlugin'}}
)
