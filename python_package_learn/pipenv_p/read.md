## 安装
pip install pipenv

## 说明
### 读取环境变量
pipenv 会自动读取.env中的环境变量,使用# 进行注释
### pipenv lock
您可以使用在您的开发环境上编译您的依赖项，并将编译后的内容部署到您的所有生产环境中以进行可重现的构建。
pipenv lockPipfile.lock
## 使用
### 安装包
pipenv install <package_name>
### 卸载包
pipenv uninstall <package_name>
### 进入虚拟环境
pipenv shell
### 使用虚拟环境运行命令
pipenv run python main.py