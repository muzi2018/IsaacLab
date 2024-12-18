"""Configuration for CENTAURO robot.

The following configurations are available:

* :obj:`CENTAURO_CFG`: Whole body Centauro robot with simple PD controller for the legs

Reference: https://github.com/UMich-BipedLab/Cassie_Model/blob/master/urdf/cassie.urdf
"""

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import ImplicitActuatorCfg
from omni.isaac.lab.assets.articulation import ArticulationCfg
from omni.isaac.lab.utils.assets import ISAACLAB_NUCLEUS_DIR

##
# Configuration
##

CENTAURO_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="/home/wang/IsaacLab/source/extensions/omni.isaac.lab_assets/data/Robots/Centauro/centauro.usd",
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            rigid_body_enabled=True,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=100.0,
            enable_gyroscopic_forces=True,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0,
            sleep_threshold=0.005,
            stabilization_threshold=0.001,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.0),
        joint_pos={
            "hip_yaw_1": -0.7,
            "hip_pitch_1": -1.3,
            "knee_pitch_1": -1.6,
            "ankle_pitch_1": -0.3,
            "ankle_yaw_1": 0.7,
            "hip_yaw_2": 0.7,
            "hip_pitch_2": 1.3,
            "knee_pitch_2": 1.6,
            "ankle_pitch_2": 0.3,
            "ankle_yaw_2": -0.7,
            "hip_yaw_3": 0.7,
            "hip_pitch_3": 1.3,
            "knee_pitch_3": 1.6,
            "ankle_pitch_3": 0.3,
            "ankle_yaw_3": -0.7,
            "hip_yaw_4": -0.7,
            "hip_pitch_4": -1.3,
            "knee_pitch_4": -1.6,
            "ankle_pitch_4": -0.3,
            "ankle_yaw_4": 0.7,
            "torso_yaw": 0.0,
            "j_arm1_1": 0.5,
            "j_arm1_2": 0.3,
            "j_arm1_3": 0.3,
            "j_arm1_4": -2.2,
            "j_arm1_5": 0.0,
            "j_arm1_6": -0.8,
            "j_arm2_1": 0.5,
            "j_arm2_2": -0.3,
            "j_arm2_3": -0.3,
            "j_arm2_4": -2.2,
            "j_arm2_5": 0.0,
            "j_arm2_6": -0.8,
            "dagana_2_claw_joint": 0.0,
            "d435_head_joint": 0.0,
            "velodyne_joint": 0.0,
            "j_wheel_1": 0.0,
            "j_wheel_2": 0.0,
            "j_wheel_3": 0.0,
            "j_wheel_4": 0.0,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "legs": ImplicitActuatorCfg(
            joint_names_expr=["hip_.*", "knee_.*", "ankle_.*", "torso_.*", "j_arm.*", "dagana.*"],
            effort_limit=2000.0,
            velocity_limit=1000.0,
            stiffness={
                ".*": 5000.0,
            },
            damping={
                ".*": 10.0,
            },
        ),
        "wheels": ImplicitActuatorCfg(
            joint_names_expr=["j_wheel_.*", "d435_.*", "velodyne_.*"],
            effort_limit=2000.0,
            velocity_limit=1000.0,
            stiffness={
                ".*": 5000.0,
            },
            damping={
                ".*": 10.0,
            },
        ),
    },
)
