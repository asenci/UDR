cmake_minimum_required(VERSION 3.15)
project(UDR)

set(CMAKE_CXX_STANDARD 14)

include_directories(src
        /usr/local/opt/libudt/include/udt
        /usr/local/opt/openssl/include)

add_executable(UDR
        src/cc.h
        src/crypto.h
        src/udr.cpp
        src/udr_log.cpp
        src/udr_options.cpp
        src/udr_options.h
        src/udr_threads.cpp
        src/udr_threads.h
        src/udr_util.cpp
        src/udr_util.h)