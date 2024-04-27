from common.login_public import *

record_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['record_data'])
report_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['template_data'])