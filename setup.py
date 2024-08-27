from setuptools import setup

setup(
    name='text_analyzer_tool',
    version='0.1',
    py_modules=['script'],  
    entry_points={
        'console_scripts': [
            'text-analyze=script:main',
        ],
    },
)
