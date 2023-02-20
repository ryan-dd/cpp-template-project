from conans import ConanFile, CMake, tools
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
import re
import os

class SampleProjectConan(ConanFile):
    name = "SampleProject"

    def set_version(self):
        content = tools.load(os.path.join(self.recipe_folder, "CMakeLists.txt"))
        version = re.search(r"set\(SampleProject_VERSION (.*)\)", content).group(1)
        self.version = version.strip()

    url = "https://github.com/ryan-dd/cpp-template-project"
    license = "MIT"
    description = "C++ template project"
    settings = "os", "compiler", "arch", "build_type"
    generators = "CMakeToolchain", "CMakeDeps"

    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto"
    }

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "build_tests": [True, False],
        "build_docs": [True, False],
        }

    default_options = {
        "shared": False,
        "fPIC": True,
        "build_tests": True,
        "build_docs": True,
        }

    def configure(self):
        if self.options.shared:
            del self.options.fPIC

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables['SampleProject_BUILD_TESTS'] = self.options.build_tests
        tc.variables['SampleProject_BUILD_DOCS'] = self.options.build_docs
        tc.generate()

    def build_requirements(self):
        if self.options.build_tests:
            self.test_requires("gtest/[>=1.8.1]")
        if self.options.build_docs:
            self.tool_requires("doxygen/[>=1.9.1]")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        tools.rmdir(os.path.join(self.package_folder, "lib", "cmake"))

    def package_info(self):
        self.cpp_info.libs.append("SampleProject")

    def package_id(self):
        # Make convenience build options have no effect on the package_id
        del self.info.options.build_tests
        del self.info.options.build_docs
