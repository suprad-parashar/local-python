import sys

language = sys.argv[1]
file_name = sys.argv[2]

with open("keywords/" + language + ".yml", 'rb') as f:
	yml_lines = [line.decode('utf-8').strip() for line in f]
	keywords = {}
	for yml_line in yml_lines:
		key, value = map(lambda x: x.strip(), yml_line.split(':', maxsplit=1))
		keywords[key] = value

with open(file_name, "rb") as f:
	lines = []
	for line in f:
		line = line.decode("utf-8")
		for key, value in keywords.items():
			line = line.replace(key, value)
		lines.append(line)
	exec("".join(lines))