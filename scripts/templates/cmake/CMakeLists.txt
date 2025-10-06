# Prevent in-source builds
if(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_BINARY_DIR})
      message(FATAL_ERROR "DO NOT BUILD in-tree.")
  endif()

cmake_minimum_required(VERSION 3.19)
project({{ELEMENT_NAME}} CXX)

# SST Configuration Sanity Check
find_program(SST sst)
if(NOT SST)
    message(FATAL_ERROR "sst not found")
endif()

find_program(SST_CONFIG sst-config)

if(NOT SST_CONFIG)
    message(FATAL_ERROR "sst-config not found")
endif()

# Use sst-config to retrieve compiler and linker flags
execute_process(COMMAND sst-config --CXX OUTPUT_VARIABLE SST_CXX OUTPUT_STRIP_TRAILING_WHITESPACE)
execute_process(COMMAND sst-config --ELEMENT_CXXFLAGS OUTPUT_VARIABLE SST_CXXFLAGS OUTPUT_STRIP_TRAILING_WHITESPACE)
execute_process(COMMAND sst-config --ELEMENT_LDFLAGS OUTPUT_VARIABLE SST_LDFLAGS OUTPUT_STRIP_TRAILING_WHITESPACE)

# Remove any flags returned with SST_CXX
string(REGEX MATCH "^[^ ]+" SST_CXX_COMPILER ${SST_CXX})

# Set the compiler and flags
set(CMAKE_CXX_COMPILER ${SST_CXX_COMPILER})
set(CMAKE_CXX_FLAGS "${SST_CXXFLAGS}")
set(CMAKE_SHARED_LINKER_FLAGS "${SST_LDFLAGS}")

add_subdirectory(src)
