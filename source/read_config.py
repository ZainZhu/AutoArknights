# 读取配置文件
import yaml

with open(r'./config.yaml', encoding="UTF-8") as f:
    config = yaml.full_load(f)
