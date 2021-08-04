import nmap3
import yaml
def scan_port(ip):
	return yaml.dump(nmap3.Nmap().scan_top_ports(ip), sort_keys=False, default_flow_style=False)
