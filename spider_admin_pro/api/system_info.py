# -*- coding: utf-8 -*-
# ==============================================
# 系统信息接口
# ==============================================
from flask import request

from spider_admin_pro.lib.flask_app.flask_app import BlueprintAppApi
from spider_admin_pro.service.auth import AuthService
from spider_admin_pro.service.system_data import SystemDataService
from spider_admin_pro.service.system_info import SystemInfoService

system_api = BlueprintAppApi("system", __name__)


@system_api.before_request
def before_request():
    token = request.headers.get('Token')
    AuthService.check_token(token)


@system_api.post('/systemInfo')
def get_system_info():
    return SystemInfoService.get_system_info()


@system_api.post("/systemData")
def get_system_data():
    return SystemDataService.get_system_data()


@system_api.post("/systemConfig")
def get_system_config():
    return SystemDataService.get_system_config()
