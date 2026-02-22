import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    parameters = json.loads('{"joint":"699a4d75d35a96c8bc11eb3a","control_mode":"position","transport":"can","units":"radians","gear_ratio":1,"smoothing_alpha":0,"can.node_id":0,"can.interface":"socketcan","can.channel":"can0","can.bitrate":1000000,"can.poll_hz":50,"can.request_iq":false,"can.heartbeat_timeout_s":2,"can.enable_closed_loop_on_start":true,"can.torque_constant":0,"limit.lower_position":0,"limit.upper_position":360,"limit.position_step":null,"limit.max_effort":0,"limit.effort_step":0.1,"limit.max_velocity":0,"limit.velocity_step":0.1}')
    configuration = json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')
    pins = json.loads('[{"pin_id":"6976bda65eb68f72bfec9b31:/joint/state","name":"/joint/state","direction":"output","msg_type":"sensor_msgs/JointState"},{"pin_id":"6976bda65eb68f72bfec9b31:/joint_controller/command","name":"/joint_controller/command","direction":"input","msg_type":"trajectory_msgs/JointTrajectory"}]')
    inbound_connections = json.loads('[]')
    outbound_connections = json.loads('[]')
    env = {
        "POLYFLOW_NODE_ID": "699a4e08d35a96c8bc11ebbf",
        "POLYFLOW_PARAMETERS": json.dumps(parameters),
        "POLYFLOW_CONFIGURATION": json.dumps(configuration),
        "POLYFLOW_PINS": json.dumps(pins),
        "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(inbound_connections),
        "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(outbound_connections),
    }

    return LaunchDescription([
        Node(
            package="odrive_s1",
            executable="odrive_s1_node",
            name="odrive_s1_node",
            output="screen",
            additional_env=env
        )
    ])