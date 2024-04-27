from common.login_public import *


threat_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['threat_data'])
domain_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['domain_data'])

