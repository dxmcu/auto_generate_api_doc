**简要描述：**

- 查询所有机器人配置信息

**请求URL：**

- `http://<IP>:<PORT>/api/v1/config/get_all_robot_config`

**请求方式：**

- GET

**请求示例：**

- `http://192.168.124.228:9999/api/v1/config/get_all_robot_config`

**请求参数**

无

**请求参数说明：**

无

**成功返回示例：**

```
{
  "errmsg": "Query_OK", 
  "errno": "0", 
  "info": [
    {
      "battery_voltage": 200.0000, 
      "footprint_c1_r": 0.8000, 
      "footprint_c1_x": 0.4000, 
      "footprint_c1_y": 0.0000, 
      "footprint_c2_r": 0.8000, 
      "footprint_c2_x": 0.0000, 
      "footprint_c2_y": 0.0000, 
      "footprint_c3_r": 0.8000, 
      "footprint_c3_x": -0.4000, 
      "footprint_c3_y": 0.0000, 
      "footprint_c4_r": -1.0000, 
      "footprint_c4_x": 0.2000, 
      "footprint_c4_y": 0.0000, 
      "footprint_c5_r": -1.0000, 
      "footprint_c5_x": 0.0000, 
      "footprint_c5_y": 0.0000, 
      "id": 1, 
      "payload": 100.0000, 
      "serial": "yg00sim018042309001n00", 
      "trajectory_mode": 1, 
      "type": "forklift"
    }, 
    {
      "battery_voltage": 48.0000, 
      "footprint_c1_r": 0.8000, 
      "footprint_c1_x": 0.4000, 
      "footprint_c1_y": 0.0000, 
      "footprint_c2_r": 0.8000, 
      "footprint_c2_x": 0.0000, 
      "footprint_c2_y": 0.0000, 
      "footprint_c3_r": 0.8000, 
      "footprint_c3_x": -0.4000, 
      "footprint_c3_y": 0.0000, 
      "footprint_c4_r": -1.0000, 
      "footprint_c4_x": 0.0000, 
      "footprint_c4_y": 0.0000, 
      "footprint_c5_r": -1.0000, 
      "footprint_c5_x": 0.0000, 
      "footprint_c5_y": 0.0000, 
      "id": 2, 
      "payload": 1000.0000, 
      "serial": "yg00sim018042309002n00", 
      "trajectory_mode": 1, 
      "type": ""
    }, 
    {
      "battery_voltage": 24.0000, 
      "footprint_c1_r": 0.3400, 
      "footprint_c1_x": -0.2200, 
      "footprint_c1_y": 0.0000, 
      "footprint_c2_r": 0.3400, 
      "footprint_c2_x": 0.2200, 
      "footprint_c2_y": 0.0000, 
      "footprint_c3_r": 0.4250, 
      "footprint_c3_x": 1.3300, 
      "footprint_c3_y": 0.0000, 
      "footprint_c4_r": 0.3400, 
      "footprint_c4_x": 0.6600, 
      "footprint_c4_y": 0.0000, 
      "footprint_c5_r": -1.0000, 
      "footprint_c5_x": 0.0000, 
      "footprint_c5_y": 0.0000, 
      "id": 3, 
      "payload": 1000.0000, 
      "serial": "yg00sim01804230900xn00", 
      "trajectory_mode": 0, 
      "type": ""
    }, 
    {
      "battery_voltage": 24.0000, 
      "footprint_c1_r": 0.3400, 
      "footprint_c1_x": -0.2200, 
      "footprint_c1_y": 0.0000, 
      "footprint_c2_r": 0.3400, 
      "footprint_c2_x": 0.2200, 
      "footprint_c2_y": 0.0000, 
      "footprint_c3_r": 0.4250, 
      "footprint_c3_x": 1.3300, 
      "footprint_c3_y": 0.0000, 
      "footprint_c4_r": 0.3400, 
      "footprint_c4_x": 0.6600, 
      "footprint_c4_y": 0.0000, 
      "footprint_c5_r": -1.0000, 
      "footprint_c5_x": 0.0000, 
      "footprint_c5_y": 0.0000, 
      "id": 4, 
      "payload": 1000.0000, 
      "serial": "yg00rvz017120415001n00", 
      "trajectory_mode": 0, 
      "type": "blueant"
    }, 
    {
      "battery_voltage": 24.0000, 
      "footprint_c1_r": 0.3400, 
      "footprint_c1_x": -0.2200, 
      "footprint_c1_y": 0.0000, 
      "footprint_c2_r": 0.3400, 
      "footprint_c2_x": 0.2200, 
      "footprint_c2_y": 0.0000, 
      "footprint_c3_r": 0.4250, 
      "footprint_c3_x": 1.3300, 
      "footprint_c3_y": 0.0000, 
      "footprint_c4_r": 0.3400, 
      "footprint_c4_x": 0.6600, 
      "footprint_c4_y": 0.0000, 
      "footprint_c5_r": -1.0000, 
      "footprint_c5_x": 0.0000, 
      "footprint_c5_y": 0.0000, 
      "id": 5, 
      "payload": 1000.0000, 
      "serial": "yg00rvz017120415002n00", 
      "trajectory_mode": 0, 
      "type": "forklift"
    }, 
    {
      "battery_voltage": 24.0000, 
      "footprint_c1_r": 0.3400, 
      "footprint_c1_x": -0.2200, 
      "footprint_c1_y": 0.0000, 
      "footprint_c2_r": 0.3400, 
      "footprint_c2_x": 0.2200, 
      "footprint_c2_y": 0.0000, 
      "footprint_c3_r": 0.4250, 
      "footprint_c3_x": 1.3300, 
      "footprint_c3_y": 0.0000, 
      "footprint_c4_r": 0.3400, 
      "footprint_c4_x": 0.6600, 
      "footprint_c4_y": 0.0000, 
      "footprint_c5_r": -1.0000, 
      "footprint_c5_x": 0.0000, 
      "footprint_c5_y": 0.0000, 
      "id": 6, 
      "payload": 1000.0000, 
      "serial": "yg00b10018120710000n00", 
      "trajectory_mode": 0, 
      "type": "forklift"
    }, 
    {
      "battery_voltage": 48.0000, 
      "footprint_c1_r": 0.8000, 
      "footprint_c1_x": 0.4000, 
      "footprint_c1_y": 0.0000, 
      "footprint_c2_r": 0.8000, 
      "footprint_c2_x": 0.0000, 
      "footprint_c2_y": 0.0000, 
      "footprint_c3_r": 0.8000, 
      "footprint_c3_x": -0.4000, 
      "footprint_c3_y": 0.0000, 
      "footprint_c4_r": -1.0000, 
      "footprint_c4_x": 0.0000, 
      "footprint_c4_y": 0.0000, 
      "footprint_c5_r": -1.0000, 
      "footprint_c5_x": 0.0000, 
      "footprint_c5_y": 0.0000, 
      "id": 7, 
      "payload": 1000.0000, 
      "serial": "yg00a00017071020001n00", 
      "trajectory_mode": 1, 
      "type": "blueant"
    }, 
    {
      "battery_voltage": 2.0000, 
      "footprint_c1_r": 0.0000, 
      "footprint_c1_x": 0.0000, 
      "footprint_c1_y": 0.0000, 
      "footprint_c2_r": 0.0000, 
      "footprint_c2_x": 0.0000, 
      "footprint_c2_y": 0.0000, 
      "footprint_c3_r": 0.0000, 
      "footprint_c3_x": 0.0000, 
      "footprint_c3_y": 0.0000, 
      "footprint_c4_r": 0.0000, 
      "footprint_c4_x": 0.0000, 
      "footprint_c4_y": 0.0000, 
      "footprint_c5_r": 0.0000, 
      "footprint_c5_x": 0.0000, 
      "footprint_c5_y": 0.0000, 
      "id": 8, 
      "payload": 0.0000, 
      "serial": "yg00sim018042309001n01", 
      "trajectory_mode": 0, 
      "type": "2"
    }, 
    {
      "battery_voltage": 2.0000, 
      "footprint_c1_r": 0.0000, 
      "footprint_c1_x": 0.0000, 
      "footprint_c1_y": 0.0000, 
      "footprint_c2_r": 0.0000, 
      "footprint_c2_x": 0.0000, 
      "footprint_c2_y": 0.0000, 
      "footprint_c3_r": 0.0000, 
      "footprint_c3_x": 0.0000, 
      "footprint_c3_y": 0.0000, 
      "footprint_c4_r": 0.0000, 
      "footprint_c4_x": 0.0000, 
      "footprint_c4_y": 0.0000, 
      "footprint_c5_r": 0.0000, 
      "footprint_c5_x": 0.0000, 
      "footprint_c5_y": 0.0000, 
      "id": 9, 
      "payload": 0.0000, 
      "serial": "yg00sim018042309001n02", 
      "trajectory_mode": 0, 
      "type": "2"
    }, 
    {
      "battery_voltage": 600.0000, 
      "footprint_c1_r": 0.0000, 
      "footprint_c1_x": 0.0000, 
      "footprint_c1_y": 0.0000, 
      "footprint_c2_r": 0.0000, 
      "footprint_c2_x": 0.0000, 
      "footprint_c2_y": 0.0000, 
      "footprint_c3_r": 0.0000, 
      "footprint_c3_x": 0.0000, 
      "footprint_c3_y": 0.0000, 
      "footprint_c4_r": 0.0000, 
      "footprint_c4_x": 0.0000, 
      "footprint_c4_y": 0.0000, 
      "footprint_c5_r": 0.0000, 
      "footprint_c5_x": 0.0000, 
      "footprint_c5_y": 0.0000, 
      "id": 10, 
      "payload": 3555.0000, 
      "serial": "yg00sim018042309001n10", 
      "trajectory_mode": 0, 
      "type": "forklift"
    }
  ]
}
```

**返回参数说明：**

|参数名|类型|说明|
|:----- |:----- |----- |
|battery_voltage|float|电池电压|
|id|int|机器人id|
|errno|string|API错误码|
|errmsg|string|错误信息|


**错误返回示例：**



**返回参数说明：**

