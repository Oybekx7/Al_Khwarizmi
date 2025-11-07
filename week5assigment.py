def update_cpu_usage(servers, usages, server_id, new_usage):
    for i in range(len(servers)):
        if servers[i] == server_id:

            usages[i] = new_usage
            return True
    return False

def decommission_idle_servers(servers, usages, threshold):
    active_servers = []
    active_usages = []
    for i in range(len(servers)):
        if usages[i] > threshold:
            active_servers.append(servers[i])
            active_usages.append(usages[i])

    return active_servers, active_usages
def flag_server_load(servers, usages, high_load_threshold):
    high_load_servers = []
    normal_load_servers = []

    for i in range(len(servers)):
        if usages[i] >= high_load_threshold:
            high_load_servers.append(servers[i])
        else:
            normal_load_servers.append(servers[i])

    return high_load_servers, normal_load_servers

def analyze_server_health(initial_servers, initial_usages, server_to_update, decommission_threshold, high_load_threshold):

    servers = initial_servers.copy()
    usages = initial_usages.copy()

    update_cpu_usage(servers, usages, server_to_update[0], server_to_update[1])

    active_servers, active_usages = decommission_idle_servers(servers, usages, decommission_threshold)

    high_load_list, normal_load_list = flag_server_load(active_servers, active_usages, high_load_threshold)

    return high_load_list, normal_load_list

servers = ["db-01", "app-01", "web-01", "cache-01"]
usages = [12.5, 88.0, 75.5, 15.0]
update_info = ["db-01", 14.0]
idle_max_usage = 18.0
high_load_min_usage = 80.0

high_load, normal_load = analyze_server_health(servers, usages, update_info, idle_max_usage, high_load_min_usage)

print(f"High load: {high_load}")
print(f"Normal load: {normal_load}")