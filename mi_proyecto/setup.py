from setuptools import setup, find_packages

setup(
    name="mi_proyecto",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "mi_proyecto=cliente.cliente:main",
        ],
    },
    author="Tu Nombre",
    author_email="tuemail@ejemplo.com",
    description="Paquete para modelar clientes en una página de compras.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tuusuario/mi_proyecto",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
