from common.login_public import *

data_packet_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['data_packet_data'])
engine_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['engine_data'])
users_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['users_data'])
role_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['role_data'])
log_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['log_data'])
