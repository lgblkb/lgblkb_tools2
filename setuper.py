import os
from lgblkb_tools import logger
from lgblkb_tools.common import utils
from setup import get_package_info

class Deployer(object):
	def __init__(self):
		pass

	@property
	def lgblkb_tools_version(self):
		return get_package_info().version

	def build_and_upload(self):
		utils.run_command('python ./setup.py sdist bdist_wheel')
		utils.run_command('twine upload dist/*')
		utils.run_command('pip install --no-cache-dir lgblkb-tools -U')
		return self

	def git_push(self,commit_message):
		# utils.run_command(f"git add -A")
		utils.run_command(f'git commit -am "v{self.lgblkb_tools_version}: {commit_message}"')
		utils.run_command(f'git push')
		return self

@logger.trace()
def main():
	deployer=Deployer()
	deployer.build_and_upload()
	# deployer.git_push(input('Git commit_message:\n') or 'Update')
	utils.run_command(f"""docker build --build-arg LGBLKB_TOOLS_VERSION="{'=='+deployer.lgblkb_tools_version}" -t lgblkb/base .""")
	# utils.run_command()

	pass

if __name__=='__main__':
	main()
