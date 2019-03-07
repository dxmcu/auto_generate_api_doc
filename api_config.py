#!/usr/bin/env python
# coding:utf-8
host_ip = "192.168.124.228"
host_port = "9999"
bito_http_api_config = {
    "robot_config": {
        "get_all_robot_config": {
            "host_ip": host_ip,
            "host_port": host_port,
            "description": "查询所有机器人配置信息",
            "interface_name": "api/v1/config/get_all_robot_config",
            "req_param": "无",
            "req_param_description": "无",
            "req_method": "GET",
            "success_resp_description": [
                {"name": "battery_voltage", "type": "float", "descrip": "电池电压"},
                {"name": "id", "type": "int", "descrip": "机器人id"},
                {"name": "errno", "type": "string", "descrip": "API错误码"},
                {"name": "errmsg", "type": "string", "descrip": "错误信息"}
            ],
            "error_resp_description": [
                {"name": "errno", "type": "string", "descrip": "API错误码"},
                {"name": "errmsg", "type": "string", "descrip": "错误信息"}
            ]
        },
        "get_robot_config": {
            "host_ip": host_ip,
            "host_port": host_port,
            "description": "根据机器人序列号查询机器人配置信息",
            "interface_name": "api/v1/config/get_robot_config?serial=yg00b10018071913000n00",
            "req_param": "无",
            "req_param_description": "无",
            "req_method": "GET",
            "success_resp_description": [
                {"name": "errno", "type": "string", "descrip": "API错误码"},
                {"name": "errmsg", "type": "string", "descrip": "错误信息"}
            ],
            "error_resp_description": [
                {"name": "errno", "type": "string", "descrip": "API错误码"},
                {"name": "errmsg", "type": "string", "descrip": "错误信息"}
            ]
        }
    }
}
