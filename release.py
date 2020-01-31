import subprocess

def run_cmd(cmd,**kwargs):
	print('cmd: ',cmd)
	return subprocess.run(cmd,**dict(dict(check=True,shell=True),**kwargs))

def main():
	run_cmd("""
rm -r dist build
bumpversion patch
pipenv lock
pipenv lock -r > requirements.txt
pipenv run python setup.py bdist_wheel
twine upload dist/*
pip install --no-cache-dir lgblkb-tools -U
pip install --no-cache-dir lgblkb-tools -U
""")
	


if __name__=='__main__':
	main()
