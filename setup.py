from setuptools import setup, find_packages
import os
import os.path as op
import uuid

ver_file = os.path.join('popylar', 'version.py')
with open(ver_file) as f:
    exec(f.read())

popylar_path = op.join(op.expanduser('~'), '.popylar')

# If UID file does not exist, then generate a UID and save to file.
# We don't overwrite an existing one in order to keep UIDs constant
# when the package is upgraded or installed in a venv.
if not os.path.exists(popylar_path):
    uid = uuid.uuid1()
    with open(popylar_path, 'a') as fhandle:
        fhandle.write(uid.hex)

PACKAGES = find_packages()

opts = dict(name=NAME,
            maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            requires=REQUIRES)


if __name__ == '__main__':
    setup(**opts)
