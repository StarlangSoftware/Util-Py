from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='NlpToolkit-Util',
    version='1.0.10',
    packages=['Util'],
    url='https://github.com/StarlangSoftware/Util-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Simple Utils',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
