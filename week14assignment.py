def load_server_config(config_list):
    config_dict = {server['ip_address']: server['hostname'] for server in config_list}
    return config_dict

def check_network_status(config_dict, active_ips):
    config_ips_set = set(config_dict.keys())
    active_ips_set = set(active_ips)

    offline_servers = config_ips_set - active_ips_set
    rogue_devices = active_ips_set - config_ips_set
    
    return offline_servers, rogue_devices

def create_outage_alert(config_dict, offline_set):

    alerts = [
        f"CRITICAL: {config_dict[i]} is DOWN ({i})"
        for i in offline_set
    ]
    alerts.sort()
    
    return alerts


config = [
    {'ip_address': "192.168.1.5", 'hostname': "Database-01"},
    {'ip_address': "192.168.1.6", 'hostname': "Web-01"},
    {'ip_address': "192.168.1.7", 'hostname': "Cache-01"}
]

pings = ["192.168.1.6", "192.168.1.7", "10.0.0.1"]

config_dict = load_server_config(config)
offline_servers, rogue_devices = check_network_status(config_dict, pings)
report = create_outage_alert(config_dict, offline_servers)

print(f"Offline Servers: {offline_servers}")
print(f"Rogue Devices: {rogue_devices}")
print(f"Report: {report}")