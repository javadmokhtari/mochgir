from setuptools import setup


setup(
    name='Mochgir',
    version='0.733',
    license='MIT',
    url='https://www.github.com/javadmokhtari/github',
    description='Translate and Analyze docx documents',
    author='Javad Mokhtari Koushyar',
    packages=(
        'mochgir',
        'mochgir.conf',
        'mochgir.conf.font'
    ),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.0',
    install_requires=[
        'requests==2.19.1',
        'python-docx==0.8.6',
        'google==2.0.1',
        'reportlab==3.4.0'
    ]
)
