from configparser import ConfigParser
import sys

def getProperties(cfg_file_path,cfg_params =('input_partition','output_partition')):
    
    cfg = ConfigParser()

    try:
        cfg.read(cfg_file_path)
        cfg_params_dict = {_param : cfg.get('paths', _param) for _param in cfg_params}
        print("Config file read is successful.")
    except :
        print("Config file read is unsuccessful. This program will now exit.")
        sys.exit(1)
    return cfg_params_dict


