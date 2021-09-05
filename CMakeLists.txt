# CMakeList.txt : CMake project for Trading212Desk, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.8)

project ("trading212-desk")

# Set C++ version
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Set Qt path
set(CMAKE_PREFIX_PATH "C:/Qt/6.1.2/msvc2019_64/")

# Set Qt Auto RCC
set(CMAKE_AUTORCC ON)


# Add source to this project's executable.
add_executable(
	Trading212Desk
	"src/main.cpp"
	resources.qrc
)

# Add Qt header files
target_include_directories(Trading212Desk PRIVATE "C:/Qt/6.1.2/msvc2019_64/include")

# Add Qt library files
find_package(Qt6 COMPONENTS Charts Qml Quick Widgets REQUIRED)
target_link_libraries(Trading212Desk Qt6::Charts Qt6::Qml Qt6::Quick Qt6::Widgets)