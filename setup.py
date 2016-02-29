# coding=utf-8
from setuptools import setup, find_packages

setup(name="instant-deeplink",
      author="Zhan Yingbo",
      author_email="yingbo.zhan@skyscanner.net",
      dependency_links=[],
      entry_points={"console_scripts": ["deeplink = deeplink.cli:deeplink",
	      				]},
      install_requires=["click",],
      version="0.7",
      packages=find_packages())