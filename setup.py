from setuptools import setup

setup(
    name="numerology_flask",
    version="0.1",
    py_modules=["numerology_flask", "ton_shin_chi", "main_app"],  # 各モジュールを指定
    install_requires=[
        "blinker==1.9.0",
        "click==8.1.8",
        "colorama==0.4.6",
        "Flask==3.1.0",
        "itsdangerous==2.2.0",
        "Jinja2==3.1.5",
        "MarkupSafe==3.0.2",
        "Werkzeug==3.1.3",
        "gunicorn"
    ],
)
