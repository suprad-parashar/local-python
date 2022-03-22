import sys
from language import language_dict
from typing import List
import tokenize

# Indentation level of the code.
INDENT_LEVEL = 0

def get_token_lines(file_name: str) -> List[List[tokenize.TokenInfo]]:
	""" Returns a list of tokenized lines from the given file. """
	token_lines = []
	with open(file_name, 'rb') as f:
		tokens = list(tokenize.tokenize(f.readline))
		line = 0
		token_line = []
		for token in tokens:
			if token.type == tokenize.ENCODING:
				continue
			if token.start[0] == line:
				token_line.append(token)
			else:
				token_lines.append(token_line)
				token_line = [token]
				line = token.start[0]
		token_lines.append(token_line)
	return token_lines

def fix_name(tokens: List[tokenize.TokenInfo]) -> List[tokenize.TokenInfo]:
	""" Fix the name tokens in the given list of tokens. """
	ignorable_types = [tokenize.COMMENT]
	i = 0
	while i < len(tokens):
		token = tokens[i]
		if token.type in ignorable_types or token.type == 62:
			i += 1
		elif token.type == tokenize.NAME:
			name = token.string
			start = i
			token_start = token.start
			i += 1
			token = tokens[i]
			while (token.type == tokenize.NAME or token.type == tokenize.ERRORTOKEN) and tokens[i - 1].end[1] == token.start[1]:
				name += token.string
				i += 1
				token = tokens[i]
			new_token = tokenize.TokenInfo(tokenize.NAME, name, token_start, (token_start[0], token_start[1] + len(name)), token.line)
			tokens = tokens[:start] + [new_token] + tokens[i:]
			i = start + 1
		else:
			i += 1
	return tokens

def replace_tokens(tokens: List[tokenize.TokenInfo], keywords_map: dict) -> str:
	""" Replace the tokens in the given list of tokens with the given keywords map. """
	global INDENT_LEVEL
	code = ""
	pos = INDENT_LEVEL
	line = 0
	for token in tokens:
		if token.type == tokenize.INDENT:
			INDENT_LEVEL += 1
			pos += 1
			continue
		elif token.type == tokenize.DEDENT:
			INDENT_LEVEL -= 1
			pos -= 1
			continue
		if token.start[0] != line:
			line = token.start[0]
			pos = INDENT_LEVEL
		code += " " * (token.start[1] - pos)
		code += keywords_map.get(token.string, token.string).replace("\n", "")
		pos = token.end[1]
	return ("\t" * INDENT_LEVEL) +  code

def run(path: str, kmap: dict):
	""" Convert and Run the local code. """
	code_lines = []	

	for token_line in get_token_lines(path):
		line = replace_tokens(fix_name(token_line), kmap)
		code_lines.append(line)

	exec("\n".join(code_lines))


# The file path of the code to be converted and run.
file_path = sys.argv[1]
# The language of the code to be converted and run.
language = language_dict[file_path.split('.')[-1][2:]]

# Load the language map.
with open("keywords/" + language + ".yml", 'rb') as f:
	yml_lines = [line.decode('utf-8').strip() for line in f]
	keywords = {}
	for yml_line in yml_lines:
		if yml_line.strip().startswith('#') or yml_line.strip() == '':
			continue
		key, value = map(lambda x: x.strip(), yml_line.split(':', maxsplit=1))
		keywords[key] = value

# Convert and Run the local python script.
code_lines = []	
for token_line in get_token_lines(file_path):
	line = replace_tokens(fix_name(token_line), keywords)
	code_lines.append(line)
exec("\n".join(code_lines))