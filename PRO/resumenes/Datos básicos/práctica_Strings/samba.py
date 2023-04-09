input_ip = "//1.1.1.1/eoi/python".lstrip("/")
path_slash_index = input_ip.index("/")
host = input_ip[:path_slash_index]
path = input_ip[path_slash_index:]
print(f"host={host}; path={path}")
