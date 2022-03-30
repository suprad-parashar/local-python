class NotIndicPythonFileException(Exception):
	"""
	Raised when a file is not in Indic Python format.
	"""
	def __init__(self, file_path) -> None:
		super().__init__(f"File {file_path} is not a indic python file.")
		self.file_path = file_path

class UnknownLanguageException(Exception):
	"""
	Raised when a IndicPy file is in an unsupported language.
	"""
	def __init__(self, language) -> None:
		super().__init__(f"Language {language} is not supported.")
		self.language = language