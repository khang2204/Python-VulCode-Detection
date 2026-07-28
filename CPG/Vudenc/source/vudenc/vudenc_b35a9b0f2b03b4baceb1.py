""" Main module for the benchmark. It reads the command line arguments, reads the benchmark configuration, 
determines the runtime mode (dynamic vs. static); if dynamic, gets the benchmark data from the server,
runs the benchmarks, and records the timer results. """
import urllib.request
from ftplib import FTP, FTP_TLS, error_perm
import time
import csv
import logging
import os.path
import pathlib
import allel
import sys
import functools
import numpy as np
import zarr
import numcodecs
from numcodecs import Blosc, LZ4, LZMA
from benchmark import config
import gzip
import shutil
def create_directory_tree(path):...
"""docstring"""
path = str(path)
pathlib.Path(path).mkdir(parents=True, exist_ok=True)
def remove_directory_tree(path):...
"""docstring"""
if os.path.exists(path):
shutil.rmtree(path, ignore_errors=True)
def fetch_data_via_ftp(ftp_config, local_directory):...
"""docstring"""
if ftp_config.enabled:
create_directory_tree(local_directory)
def fetch_data_via_ftp_recursive(ftp, local_directory, remote_directory,...
if ftp_config.use_tls:
"""docstring"""
ftp = FTP_TLS(ftp_config.server)
ftp = FTP(ftp_config.server)
if remote_subdirs_list is not None and len(remote_subdirs_list) > 0:
ftp.login(ftp_config.username, ftp_config.password)
ftp.login(ftp_config.username, ftp_config.password)
remote_path_relative = '/'.join(remote_subdirs_list)
remote_subdirs_list = []
ftp.prot_p()
if not ftp_config.files:
remote_path_absolute = ('/' + remote_directory + '/' + remote_path_relative +
    '/')
remote_path_relative = ''
fetch_data_via_ftp_recursive(ftp=ftp, local_directory=local_directory,
    remote_directory=ftp_config.directory)
ftp.cwd(ftp_config.directory)
local_path = local_directory + '/' + remote_path_relative
print('[Setup][FTP] Error: Could not change to: {}'.format(
    remote_path_absolute))
ftp.cwd(remote_path_absolute)
remote_path_absolute = '/' + remote_directory + '/'
ftp.close()
file_counter = 1
os.mkdir(local_path)
file_list = ftp.nlst()
file_list_total = len(ftp_config.files)
print('[Setup][FTP] Created local folder: {}'.format(local_path))
file_counter = 1
for remote_filename in ftp_config.files:
file_list_total = len(file_list)
local_filename = remote_filename
for file in file_list:
filepath = os.path.join(local_directory, local_filename)
file_path_local = local_directory + '/' + remote_path_relative + '/' + file
def fetch_file_from_url(url, local_file):...
if not os.path.exists(filepath):
if not os.path.isfile(file_path_local):
urllib.request.urlretrieve(url, local_file)
print('[Setup][FTP] ({}/{}) File already exists. Skipping: {}'.format(
    file_counter, file_list_total, filepath))
ftp.retrbinary('RETR %s' % remote_filename, local_file.write)
print('[Setup][FTP] ({}/{}) Error downloading file. Skipping: {}'.format(
    file_counter, file_list_total, filepath))
file_counter = file_counter + 1
print('[Setup][FTP] ({}/{}) File already exists. Skipping: {}'.format(
    file_counter, file_list_total, file_path_local))
ftp.cwd(remote_path_absolute + file)
temp = ftp.nlst()
file_counter = file_counter + 1
def decompress_gzip(local_file_gz, local_file):...
print('[Setup][FTP] ({}/{}) File downloaded: {}'.format(file_counter,
    file_list_total, filepath))
local_file.close()
print('[Setup][FTP] Switching to directory: {}'.format(remote_path_relative +
    '/' + file))
if not os.path.isfile(file_path_local):
shutil.copyfileobj(file_in, file_out)
os.remove(filepath)
new_remote_subdirs_list = remote_subdirs_list.copy()
ftp.retrbinary('RETR {}'.format(file), local_file.write)
def process_data_files(input_dir, temp_dir, output_dir):...
new_remote_subdirs_list.append(file)
print('[Setup][FTP] ({}/{}) File downloaded: {}'.format(file_counter,
    file_list_total, file_path_local))
"""docstring"""
fetch_data_via_ftp_recursive(ftp=ftp, local_directory=local_directory,
    remote_directory=remote_directory, remote_subdirs_list=
    new_remote_subdirs_list)
input_dir = str(input_dir)
ftp.cwd(remote_path_absolute)
temp_dir = str(temp_dir)
output_dir = str(output_dir)
create_directory_tree(input_dir)
create_directory_tree(temp_dir)
create_directory_tree(output_dir)
pathlist_gz = pathlib.Path(input_dir).glob('**/*.gz')
for path in pathlist_gz:
path_str = str(path)
pathlist_vcf_temp = pathlib.Path(temp_dir).glob('**/*.vcf')
file_output_str = path_leaf(path_str)
for path in pathlist_vcf_temp:
file_output_str = file_output_str[0:len(file_output_str) - 3]
path_temp_str = str(path)
remove_directory_tree(temp_dir)
path_temp_output = str(pathlib.Path(temp_dir, file_output_str))
filename_str = path_leaf(path_temp_str)
pathlist_vcf_input = pathlib.Path(input_dir).glob('**/*.vcf')
print('[Setup][Data] Decompressing file: {}'.format(path_str))
path_vcf_str = str(pathlib.Path(output_dir, filename_str))
for path in pathlist_vcf_input:
print('  - Output: {}'.format(path_temp_output))
shutil.move(path_temp_str, path_vcf_str)
path_input_str = str(path)
def path_head(path):...
decompress_gzip(path_str, path_temp_output)
filename_str = path_leaf(path_input_str)
head, tail = os.path.split(path)
path_vcf_str = str(pathlib.Path(output_dir, filename_str))
return head
shutil.copy(path_input_str, path_vcf_str)
