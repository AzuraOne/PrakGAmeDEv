from setuptools import setup

setup(
    name="asteroids",
    options={
        'build_apps':{
            'gui_apps':{
                'asteroids':'main.py',
            },
            'log_filename': '$USER_APPDATA/Asteroids/output.log',
            'log_append': False,

            'include_patterns': [
                '**/*.png',
                '**/*.jpg',
                '**/*.egg',
            ],
            'plugin': [
                'pandagl',
                'p3openal_audio',
                

            ],
        }
    }
)