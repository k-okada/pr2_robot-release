Name:           ros-indigo-pr2-bringup
Version:        1.6.10
Release:        1%{?dist}
Summary:        ROS pr2_bringup package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_bringup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-diagnostic-aggregator
Requires:       ros-indigo-ethercat-trigger-controllers
Requires:       ros-indigo-hokuyo-node
Requires:       ros-indigo-joint-trajectory-action
Requires:       ros-indigo-joy
Requires:       ros-indigo-microstrain-3dmgx2-imu
Requires:       ros-indigo-ocean-battery-driver
Requires:       ros-indigo-power-monitor
Requires:       ros-indigo-pr2-calibration-controllers
Requires:       ros-indigo-pr2-camera-synchronizer
Requires:       ros-indigo-pr2-computer-monitor
Requires:       ros-indigo-pr2-controller-configuration
Requires:       ros-indigo-pr2-controller-manager
Requires:       ros-indigo-pr2-dashboard-aggregator
Requires:       ros-indigo-pr2-description
Requires:       ros-indigo-pr2-ethercat
Requires:       ros-indigo-pr2-gripper-action
Requires:       ros-indigo-pr2-head-action
Requires:       ros-indigo-pr2-machine
Requires:       ros-indigo-pr2-power-board
Requires:       ros-indigo-pr2-run-stop-auto-restart
Requires:       ros-indigo-prosilica-camera
Requires:       ros-indigo-robot-mechanism-controllers
Requires:       ros-indigo-robot-pose-ekf
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-rosbag
Requires:       ros-indigo-single-joint-position-action
Requires:       ros-indigo-sound-play
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-stereo-image-proc
Requires:       ros-indigo-tf2-ros
Requires:       ros-indigo-wge100-camera
Requires:       ros-indigo-wifi-ddwrt
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rostest

%description
Launch files and scripts needed to bring a PR2 up into a running state.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Dec 04 2015 Devon Ash <ahendrix@willowgarage.com> - 1.6.10-1
- Autogenerated by Bloom

* Wed Sep 16 2015 Devon Ash <ahendrix@willowgarage.com> - 1.6.10-0
- Autogenerated by Bloom

* Tue Sep 01 2015 Austin Hendrix <ahendrix@willowgarage.com> - 1.6.9-0
- Autogenerated by Bloom

* Fri Feb 13 2015 Austin Hendrix <ahendrix@willowgarage.com> - 1.6.7-0
- Autogenerated by Bloom

