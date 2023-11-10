import setuptools
setuptools.setup(
    name='math-quiz',
    version='0.0',
    packages=setuptools.find_packages(),
    install_requires = [],
    author='ParamPatel-re95xojo-FAU',
    description='math_quiz package',
    url='https://github.com/Param-Patel/dss_homework_ex01',
    long_description = 'Math quiz package. Generate a random number(generate_random_number func) '
                       'and a random operator [+,*,-] (generate_random_operator func).'
                       'Calculates the result and prompts user to give answer. '
                       'Scores the user answer and displays the total score/total questions',
    zip_safe = False,
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',
        ],
    }
)
