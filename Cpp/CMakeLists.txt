cmake_minimum_required(VERSION 3.31)
project(AtcoderExercise
    VERSION 0.1.0
    LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED True)


set(EXECUTABLES
    ABC086A
    ABC081A
)

foreach(EXEC ${EXECUTABLES})
    add_executable(${EXEC} src/${EXEC}.cpp)
endforeach()
