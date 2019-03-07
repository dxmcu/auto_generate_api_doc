#!/usr/bin/env python
# coding:utf-8
import json
import os

import requests
import sys

from auto_generate_api_doc import api_config
from auto_generate_api_doc.markdown_to_reStructedText import md_to_rst

reload(sys)
sys.setdefaultencoding('utf8')

doc = "**简要描述：**\n\n- %(description)s\n\n**请求URL：**\n\n- %(req_url_sample)s" \
      "\n\n**请求方式：**\n\n- %(req_method)s\n\n**请求示例：**\n\n- %(req_url_example)s\n\n**请求参数**" \
      "\n\n%(req_param)s\n\n**请求参数说明：**\n\n%(req_param_description)s\n\n**成功返回示例：** \n\n%(success_resp)s" \
      "\n\n**返回参数说明：**\n\n%(success_resp_description)s\n\n**错误返回示例：**\n\n**返回参数说明：**\n\n|参数名|类型|说明|" \
      "\n|:-----  |:-----|-----|\n|errno |string   |API错误码|\n|errmsg |string   |错误信息|"
doc_dic = dict()
doc_str = ""
for key, value in api_config.bito_http_api_config.items():
    print key
    if not os.path.exists("bito_http_api/{}".format(key)):
        os.makedirs("bito_http_api/{}".format(key))
    for key1, value1 in value.items():
        doc_dic["description"] = value1["description"]
        doc_dic["req_url_sample"] = "`http://<IP>:<PORT>/{}`".format(value1["interface_name"])
        doc_dic["req_method"] = value1["req_method"]
        doc_dic["req_url_example"] = "`http://{}:{}/{}`".format(value1["host_ip"], value1["host_port"],
                                                                value1["interface_name"])
        if value1["req_param"] == "无":
            doc_dic["req_param"] = value1["req_param"]
        else:
            doc_dic["req_param"] = '```\n' + value1["req_param"] + '```'
        if value1["req_param_description"] == "无":
            doc_dic["req_param_description"] = value1["req_param_description"]
        else:
            s1 = "|参数名|必选|类型|说明|\n|:---- |:--- |:----- |-----|\n"
            for k, v in value1["req_param_description"]:
                s1 = s1 + "|{}|{}|{}|{}|\n".format(k, v["is_need"], v["type"], v["descrip"])
        url = "http://{}:{}/{}".format(value1["host_ip"], value1["host_port"], value1["interface_name"])
        if value1["req_method"] == "GET":
            resp = requests.get(url)
        elif value1["req_method"] == "POST":
            if value1["req_param"] != "无":
                data = json.dumps(value1["req_param"])
                resp = requests.post(url, data=data, headers={'Content-Type': 'application/json'})
            else:
                resp = requests.post(url)
        elif value1["req_method"] == "PUT":
            if value1["req_param"] != "无":
                data = json.dumps(value1["req_param"])
                resp = requests.put(url, data=data, headers={'Content-Type': 'application/json'})
            else:
                resp = requests.put(url)
        elif value1["req_method"] == "DELETE":
            if value1["req_param"] != "无":
                data = json.dumps(value1["req_param"])
                resp = requests.delete(url, data=data, headers={'Content-Type': 'application/json'})
            else:
                resp = requests.delete(url)
        else:
            print "req_method is error: {}".format(value1["req_method"])
        s2 = "|参数名|类型|说明|\n|:----- |:----- |----- |\n"
        res = json.loads(resp.text)
        if res["errno"] == "0":
            doc_dic["success_resp"] = '```\n' + resp.text + '```'
            doc_dic["error_resp"] = ""
            if value1["success_resp_description"]:
                for param in value1["success_resp_description"]:
                    s2 += '|{}|{}|{}|\n'.format(param["name"], param["type"], param["descrip"])
            doc_dic["success_resp_description"] = s2
            doc_dic["error_resp_description"] = ""
        else:
            doc_dic["error_resp"] = '```\n' + resp.text + '```'
            doc_dic["success_resp"] = ""
            if value1["error_resp_description"]:
                for param in value1["error_resp_description"]:
                    s2 += '|{}|{}|{}|\n'.format(param["name"], param["type"], param["descrip"])
            doc_dic["error_resp_description"] = s2
            doc_dic["success_resp_description"] = ""
        with open("bito_http_api/{}/{}.md".format(key, key1), 'w') as f:
            finally_md = "**简要描述：**\n\n- %(description)s\n\n" \
                         "**请求URL：**\n\n- %(req_url_sample)s\n\n" \
                         "**请求方式：**\n\n- %(req_method)s\n\n" \
                         "**请求示例：**\n\n- %(req_url_example)s\n\n" \
                         "**请求参数**\n\n%(req_param)s\n\n" \
                         "**请求参数说明：**\n\n%(req_param_description)s\n\n" \
                         "**成功返回示例：**\n\n%(success_resp)s\n\n" \
                         "**返回参数说明：**\n\n%(success_resp_description)s\n\n" \
                         "**错误返回示例：**\n\n%(error_resp)s\n\n" \
                         "**返回参数说明：**\n\n%(error_resp_description)s" % doc_dic
            f.write(finally_md)
        md_to_rst("bito_http_api/{}/{}.md".format(key, key1), "bito_http_api/{}/{}.rst".format(key, key1))
        print "\t", key1
print 'Complete.....'
