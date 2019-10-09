import os

from lgblkb_tools.common import utils
from setup import get_package_info

class Deployer(object):
	def __init__(self):
		pass

	def build_and_upload(self):
		utils.run_command('python ./setup.py sdist bdist_wheel')
		utils.run_command('twine upload dist/*')
		utils.run_command('pip install --no-cache-dir lgblkb-tools -U')
		return self

	def git_push(self,commit_message):
		lgblkb_tools_version=get_package_info().version
		# utils.run_command(f"git add -A")
		utils.run_command(f'git commit -am "v{lgblkb_tools_version}: {commit_message}"')
		utils.run_command(f'git push')
		return self

def main():
	from lgblkb_tools.remote import SshMan
	import fabric
	# sshman=SshMan(fabric.Connection())
	# return
	deployer=Deployer()
	deployer.build_and_upload()
	deployer.git_push(input('Git commit_message:\n') or 'Update')


	# utils.run_command(f'docker build -t lgblkb_base .')

	pass

if __name__=='__main__':
	main()
