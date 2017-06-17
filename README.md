# 豆豆空间服务端代码

## 搭建虚拟开发环境

### 安装virtualenv

```sh 
pip install virtualenv
```

### 创建一个独立的Python环境venv

```sh
virtualenv --no-site-packages venv
```

### 使用这个venv环境

```sh
source venv/bin/activate
```

### 离开venv 环境

```sh
deactivte
```

### 安装项目依赖

```sh 
pip install -r requirements.txt
```

