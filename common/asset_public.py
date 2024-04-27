from common.login_public import *
asset_management_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['management_data'])
asset_allocation_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['allocation_data'])
asset_discovery_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['discovery_data'])
asset_scan_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['scan_data'])
asset_topology_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['topology_data'])
autogenerate_file = a.translate_path(a.read_yml_file(config)['item'], a.read_yml_file(config)['autogenerate_data'])
