import inspect
from API.Api_action import *


class topology:

    def __init__(self):
        self.method = Api_method()

    @allure.step("查看通讯拓扑网段视角层级")
    def topology_getNetworkSegmentTopo(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("资产关联视角层级")
    def topology_getAssetRelationView(self, linkcount, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route + linkcount
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("组织管理视角层级")
    def topology_getTopoByOrg(self, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("通讯拓扑详情")
    def topology_getTopoByNetworkSegment(self, network, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route + network
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp

    @allure.step("资产详情")
    def topology_getTopoByOrgId(self, orgId, cookie):
        url_route = inspect.currentframe().f_code.co_name.replace('_', '/')
        url = Public().handle_str() + '/tsa/v1.1/api/' + url_route + orgId
        rsp = self.method.http_get(url, None, None, cookie)
        return rsp
