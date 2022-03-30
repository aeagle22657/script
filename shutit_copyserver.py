from shutit_module import ShutItModule

class shutit_copyserver(ShutItModule):


	def build(self, shutit):

		return True

	def get_config(self, shutit):

		return True

	def test(self, shutit):

		return True

	def finalize(self, shutit):

		return True

	def is_installed(self, shutit):

		return False

	def start(self, shutit):

		return True

	def stop(self, shutit):

		return True

def module():
	return shutit_copyserver(
		'shutit.copied_server.shutit_copyserver', 521189402.0001,
		description='',
		maintainer='',
		delivery_methods=['docker'],
		depends=['shutit.tk.setup']
	)