#!/usr/bin/env python

import os
import csv


SOURCE_FILE_NAME = 'credentials.csv'
FILE_AWS_NAME = 'credentials'
FILE_CONFIG_AWS_NAME = 'config'
DIR_NAME = 'AWS'
REGION = 'eu-west-1'


def main():
    filename = SOURCE_FILE_NAME
    if not check_file_present(filename):
        print(f"File {filename} is not present, for more info check \
            'https://signin.aws.amazon.com/'")
        return
    save_datatofile(filename)


def create_aws_dir(dir_name):
    homedir = os.path.expanduser("~")
    pathforawsdir = os.path.join(homedir, dir_name)
    if not os.path.isdir(pathforawsdir):
        os.mkdir(pathforawsdir)
    # else:
    #     print(f'Directory {pathforawsdir} exists'
    return pathforawsdir



def save_datatofile(filename):
    dir_aws_name = DIR_NAME
    file_aws_name = FILE_AWS_NAME

    awsdirpath = create_aws_dir(dir_aws_name)
    awsfile = (os.path.join(awsdirpath, file_aws_name))
    write_data_file(awsfile, get_info(filename))


    file_config_aws_name = FILE_CONFIG_AWS_NAME  
    region = 'region = ' + REGION
    towrite = ['[default]', region]
    configfile = (os.path.join(awsdirpath, file_config_aws_name))
    write_data_file(configfile, towrite)


def write_data_file(filename, data):
    with open(filename, 'w') as file:
        file.write('\n'.join(data))  


def check_file_present(file_name):
    current_path = os.getcwd()
    filepath = os.path.join(current_path, file_name)
    return os.path.isfile(filepath)


def get_info(filename):
    default = '[default]'
    access_key_for_write = 'aws_access_key_id = ' 
    secret_key_for_write = 'aws_secret_access_key = '
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            access_key_for_write += row['Access key ID']
            secret_key_for_write += row['Secret access key']
    return [default, access_key_for_write, secret_key_for_write, '\n']       


if __name__ == '__main__':
    main()

