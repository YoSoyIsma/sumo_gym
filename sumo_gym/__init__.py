from gym.envs.registration import registry, register, make, spec
import xml.etree.ElementTree as ET

# Toy Text
# ----------------------------------------
def get_traffic_light_junction_lanes_dict():
    junction_lanes_dict = {}
    source_net_file = 'C:/Users/Ismael/Desktop/New folder/Reinforcement_learning_project_traffic-signal-control-master/sumo_env/four_intersects.net.xml'
    tree = ET.parse(source_net_file)
    root = tree.getroot()
    for junction in root.findall('junction'):
        junction_type = junction.get('type')
        if junction_type == 'traffic_light':
            junction_id = junction.get('id')
            junction_inc_lanes_list = junction.get('incLanes').split(' ')
            junction_lanes_dict[junction_id] = junction_inc_lanes_list
    return junction_lanes_dict

register(
    id='FourIntersects-v1',
    entry_point= 'sumo_gym.envs:FourIntersectsEnv',
    kwargs={'traffic_light_junction_lanes_dict' : get_traffic_light_junction_lanes_dict(),
            'version_num' : 1},
    max_episode_steps=1000,
)
