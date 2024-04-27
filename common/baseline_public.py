from common.login_public import *

asset_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['asset_data'])
protocol_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['protocol_data'])
link_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['link_data'])
flow_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['flow_data'])
business_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['business_data'])
