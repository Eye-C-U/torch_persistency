from setuptools import setup, find_packages
from dog_identifier import VERSION

setup(
    name="torch_persistency",
    version=VERSION,
    packages=(
        find_packages() +
        find_packages(where = "torch_persistency")
    ),
    include_package_data=True,
    zip_safe=False
)