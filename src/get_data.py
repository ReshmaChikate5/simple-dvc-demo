# read params
# process
# return a dataframe

import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    # print(config)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    return df

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    print('args', args)
    parsed_args = args.parse_args()
    print('parsed_args :', parsed_args)
    print("----------------------------")
    print(parsed_args.config)
    data = get_data(config_path=parsed_args.config)
    print(data.head())