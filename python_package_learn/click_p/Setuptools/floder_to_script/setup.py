from setuptools import setup, find_packages

setup(
    # 查找的文件夹名称
    name='mypackage',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        # myscript1是生成的脚本的名称,
        #mypackage.scripts.myscript 是相对的文件位置
        # cli是命令名称
        myscript2=mypackage.scripts.myscript:cli
    ''',
)
