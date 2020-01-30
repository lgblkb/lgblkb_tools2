import shlex
import os
import subprocess

# from lgblkb_tools import logger
# from lgblkb_tools.common import utils
# from setup import get_package_info

#cc54c7b86b21c74409d32e50d15b6716398ce38f

def run_cmd(cmd,**kwargs):
	print('cmd: ',cmd)
	return subprocess.run(cmd,**dict(dict(check=True,shell=True),**kwargs))

class Deployer(object):
	def __init__(self):
		self.recent_docker_build=''
		pass
	
	# @property
	# def lgblkb_tools_version(self):
	# 	return get_package_info().version
	
	def build_upload_pypi(self):
		run_cmd("""
python ./setup.py sdist bdist_wheel
twine upload dist/*
pip install --no-cache-dir lgblkb-tools -U
""")
		return self
	
	# def git_push(self,commit_message):
	# 	# utils.run_cmd(f"git add -A")
	# 	run_cmd(f'git commit -am "v{self.lgblkb_tools_version}: {commit_message}"')
	# 	run_cmd(f'git push')
	# 	return self
	
	def build_s2_base(self):
		run_cmd("""
cd /home/lgblkb/PycharmProjects/lgblkb_tools2/s2base
docker build -t lgblkb/s2base .
""")
		# utils.run_cmd("""
		# cd /home/lgblkb/PycharmProjects/lgblkb_tools2/s2base
		# docker build -t lgblkb/s2base .""")
		self.recent_docker_build='s2base'
		return self
	
	def push(self,image_name=''):
		if not image_name:
			assert self.recent_docker_build
			image_name=self.recent_docker_build
		# utils.run_cmd(f'docker push lgblkb/{image_name}')
		subprocess.run(f'docker push lgblkb/{image_name}',shell=True,check=True)
		self.recent_docker_build=''
	
	# def build_lgblkb_base(self):
	# 	# utils.run_cmd(f"""
	# 	subprocess.run(f"""
	# 	docker build --build-arg LGBLKB_TOOLS_VERSION="{'=='+self.lgblkb_tools_version}" -t lgblkb/base .
	# 	""",shell=True,check=True)
	# 	self.recent_docker_build='base'
	# 	return self

# @logger.trace()
def main():
	deployer=Deployer()
	# deployer.build_upload_pypi()
	# deployer.build_s2_base().push()
	# deployer.build_lgblkb_base().push()
	# deployer.git_push(input('Git commit_message:\n') or 'Update')
	return
	run_cmd(f"""
	cd /home/lgblkb/PycharmProjects/imagination
	docker-compose build""")
	pass

if __name__=='__main__':
	main()
