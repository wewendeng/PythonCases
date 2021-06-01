import json
from configparser import ConfigParser
import os
from json import JSONDecodeError


class GetConfig:

    @staticmethod
    def get_conf_ini(section=None, option=None):
        """
        使用configparser模块读取ini配置文件：
        1.指定section和option时，返回对应的内容
        2.不指定section和option时，以字典形式返回config文件所有内容
        3.section是类别，option是类别下的某个选项
        """
        conf_path = os.path.dirname(__file__) + '/config.ini'
        config = ConfigParser()
        config.read(conf_path)

        if not section and not option:
            conf = {section: config.items(section) for section in config.sections()}
            return conf
        elif config.has_section(section) and not option:
            conf = config.items(section)
            return conf
        elif config.has_section(section) and option:
            conf = config.get(section, option)
            return conf
        else:
            return 'section or option not exist'

    @staticmethod
    def get_conf_json(section=None, option=None):
        conf_path = os.path.dirname(__file__) + '/config.json'
        with open(conf_path) as con:
            try:
                conf = json.loads(con.read())
            except JSONDecodeError as err:
                return err

            if not section and not option:
                return conf
            elif conf[section] and not option:
                return conf[section]
            elif conf[section] and conf[section][option]:
                return conf[section][option]
            else:
                return 'section or option not exist'


if __name__ == '__main__':
    conf = GetConfig()
    confs = conf.get_conf_json('mongo', 'username')
    print(confs)
