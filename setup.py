import setuptools

setuptools.setup(
    name='mac-screensaver',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/.screensaver-name.applescript','scripts/.screensaver-names.applescript','scripts/screensaver','scripts/screensaver-name','scripts/screensaver-names','scripts/screensaver-pid','scripts/screensaver-start','scripts/screensaver-stop','scripts/screensaver-wait']
)
