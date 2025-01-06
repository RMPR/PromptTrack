What helped: https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14

test: python -m unittest -v test/mdetr_test.py

before uploading 
compile the library: python setup.py sdist bdist_wheel
check the build: twine check dist/*
upload to pypi: twine upload dist/* else: twine upload --skip-existing dist/*


