#!/usr/bin/env python

# Author: Trevor Perrin
# See the LICENSE file for legal information regarding use of this file.

from distutils.core import setup



setup(name="tlslite-ng",
      version="0.5.0-beta4",
      author="Hubert Kario",
      author_email="hkario@redhat.com",
      url="https://github.com/tomato42/tlslite-ng",
      description="Pure python implementation of SSL and TLS.",
      license="LGPLv2",
      scripts=["scripts/tls.py", "scripts/tlsdb.py"],
      packages=["tlslite", "tlslite.utils", "tlslite.integration"],
      package_data={
                    'package1': ['LICENSE', 'README.md']},
      obsoletes=["tlslite"],
      classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Topic :: Security :: Cryptography',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: System :: Networking'
          ],
      keywords="ssl, tls, pure-python"
      )
