from common.login_public import *

audits_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['audits_data'])
kbi_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['kbi_data'])
