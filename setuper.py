import os

from lgblkb_tools.common import utils
from setup import get_package_info

def main():
	utils.run_command('python ./setup.py sdist bdist_wheel')
	utils.run_command('twine upload dist/*')
	utils.run_command('pip install --no-cache-dir lgblkb-tools -U')

	commit_message=input('Git commit_message:\n')
	utils.run_command(f'git commit -m "{commit_message}"')
	utils.run_command(f'git push')

	# lgblkb_tools_version=get_package_info().version
	# os.environ['LGBLKB_TOOLS_VERSION']=lgblkb_tools_version
	# utils.run_command(f'docker build -t lgblkb_base .')
	# utils.run_command(f'docker tag ')
	pass

if __name__=='__main__':
	main()
