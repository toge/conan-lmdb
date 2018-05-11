from conans import ConanFile, CMake, tools, AutoToolsBuildEnvironment
import os

class LmdbConan(ConanFile):
    name = "lmdb"
    version = "0.9.22"
    license = "OpenLDAP Public License"
    url = "https://github.com/LMDB/lmdb/"
    description = "Lightning Memory-Mapped Database from Symas"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/LMDB/lmdb")
        self.run("cd lmdb && git checkout LMDB_" + self.version)

    def build(self):
        os.chdir("lmdb/libraries/liblmdb/")
        autotools = AutoToolsBuildEnvironment(self)
        autotools.make(target="liblmdb.a")

        # Explicit way:
        # self.run('cmake %s/hello %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("lmdb.h", dst="include", src="lmdb/libraries/liblmdb", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["lmdb"]
