from setuptools import setup, Extension
from torch.utils import cpp_extension

setup(name='cpp_ext',
      ext_modules=[cpp_extension.CppExtension('cpp_ext', ['cpp_ext.cpp'])],
      cmdclass={'build_ext': cpp_extension.BuildExtension})