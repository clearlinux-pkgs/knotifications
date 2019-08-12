#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : knotifications
Version  : 5.61.0
Release  : 20
URL      : https://download.kde.org/stable/frameworks/5.61/knotifications-5.61.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.61/knotifications-5.61.0.tar.xz
Source1 : https://download.kde.org/stable/frameworks/5.61/knotifications-5.61.0.tar.xz.sig
Summary  : Abstraction for system notifications
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: knotifications-data = %{version}-%{release}
Requires: knotifications-lib = %{version}-%{release}
Requires: knotifications-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libcanberra-dev
BuildRequires : pkgconfig(dbusmenu-qt5)
BuildRequires : qtbase-dev mesa-dev

%description
# KNotification
Desktop notifications
## Introduction
KNotification is used to notify the user of an event. It covers feedback and
persistent events.

%package data
Summary: data components for the knotifications package.
Group: Data

%description data
data components for the knotifications package.


%package dev
Summary: dev components for the knotifications package.
Group: Development
Requires: knotifications-lib = %{version}-%{release}
Requires: knotifications-data = %{version}-%{release}
Provides: knotifications-devel = %{version}-%{release}
Requires: knotifications = %{version}-%{release}
Requires: knotifications = %{version}-%{release}

%description dev
dev components for the knotifications package.


%package lib
Summary: lib components for the knotifications package.
Group: Libraries
Requires: knotifications-data = %{version}-%{release}
Requires: knotifications-license = %{version}-%{release}

%description lib
lib components for the knotifications package.


%package license
Summary: license components for the knotifications package.
Group: Default

%description license
license components for the knotifications package.


%prep
%setup -q -n knotifications-5.61.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565593784
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1565593784
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/knotifications
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/knotifications/COPYING-CMAKE-SCRIPTS
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/knotifications/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf5_org.kde.StatusNotifierItem.xml
/usr/share/dbus-1/interfaces/kf5_org.kde.StatusNotifierWatcher.xml
/usr/share/kservicetypes5/knotificationplugin.desktop
/usr/share/locale/af/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/as/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/be/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/br/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/crh/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/csb/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/da/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/de/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/el/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/es/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/et/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ha/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/he/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/hne/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/hy/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/id/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/is/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/it/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/km/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/kn/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/oc/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/or/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ps/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/se/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/si/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/te/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/th/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/tt/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/knotifications5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/knotifications5_qt.qm
/usr/share/qlogging-categories5/knotifications.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KNotifications/KNotification
/usr/include/KF5/KNotifications/KNotificationPlugin
/usr/include/KF5/KNotifications/KNotificationRestrictions
/usr/include/KF5/KNotifications/KNotifyConfig
/usr/include/KF5/KNotifications/KPassivePopup
/usr/include/KF5/KNotifications/KStatusNotifierItem
/usr/include/KF5/KNotifications/knotification.h
/usr/include/KF5/KNotifications/knotificationplugin.h
/usr/include/KF5/KNotifications/knotificationrestrictions.h
/usr/include/KF5/KNotifications/knotifications_export.h
/usr/include/KF5/KNotifications/knotifyconfig.h
/usr/include/KF5/KNotifications/kpassivepopup.h
/usr/include/KF5/KNotifications/kstatusnotifieritem.h
/usr/include/KF5/knotifications_version.h
/usr/lib64/cmake/KF5Notifications/KF5NotificationsConfig.cmake
/usr/lib64/cmake/KF5Notifications/KF5NotificationsConfigVersion.cmake
/usr/lib64/cmake/KF5Notifications/KF5NotificationsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Notifications/KF5NotificationsTargets.cmake
/usr/lib64/libKF5Notifications.so
/usr/lib64/qt5/mkspecs/modules/qt_KNotifications.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Notifications.so.5
/usr/lib64/libKF5Notifications.so.5.61.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/knotifications/COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/knotifications/COPYING.LIB
