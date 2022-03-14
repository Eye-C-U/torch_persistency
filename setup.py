from setuptools import setup, find_packages
from torch_persistency import VERSION

setup(
    name="torch_model_persistency",
    version=VERSION,
    packages=(
        find_packages() +
        find_packages(where = "torch_persistency")
    ),
    include_package_data=True,
    zip_safe=False
)