# %{_bindir}/nextcloud needs rpath to find its helper
# libraries in %{_libdir}/nextcloud
%global dont_remote_rpath 1

%define libname %mklibname nextcloudsync 2
%define devname %mklibname -d nextcloudsync

Summary:	Client for the NextCloud cloud storage system
Name:		nextcloud-client
Version:	3.10.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://github.com/nextcloud/desktop
Source0:	https://github.com/nextcloud/desktop/archive/v%{version}/desktop-%{version}.tar.gz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Keychain)
BuildRequires:	cmake(Qt5WebSockets)
BuildRequires:	cmake(DolphinVcs) < 23.05.90
BuildRequires:  doxygen
BuildRequires:  inotify-tools
BuildRequires:  inotifytools-devel
#BuildRequires:  pkgconfig(cloudproviders)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	python >= 3.0
BuildRequires:	texlive
BuildRequires:	python-sphinx
BuildRequires:	inkscape
Requires:	%{libname} = %{EVRD}
Recommends:	%{name}-dolphin = %{EVRD}

%description
Client for the NextCloud cloud storage system

%package dolphin
Summary:	NextCloud integration for the Dolphin file manager
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
Enhances:	dolphin

%description dolphin
NextCloud integration for the Dolphin file manager

%package nautilus
Summary:	NextCloud integration for the Nautilus file manager
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
Enhances:	nautilus

%description nautilus
NextCloud integration for the Nautilus file manager

%package caja
Summary:	NextCloud integration for the Caja file manager
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
Enhances:	caja

%description caja
NextCloud integration for the Caja file manager

%package -n %{libname}
Summary:	Library for NextCloud synchronization
Group:		System/Libraries

%description -n %{libname}
Library for NextCloud synchronization

%package -n %{devname}
Summary:	Development files for NextCloud synchronization
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for NextCloud synchronization

%files -n %{libname}
%{_libdir}/libnextcloudsync.so.*
%{_libdir}/libnextcloud_csync.so.*

%files -n %{devname}
%{_libdir}/libnextcloudsync.so
%{_libdir}/libnextcloud_csync.so
%{_libdir}/nextcloudsync_vfs_suffix.so
%{_libdir}/nextcloudsync_vfs_xattr.so
%{_includedir}/nextcloudsync

%files
#{_libdir}/nextcloud
%{_datadir}/nemo-python
%{_datadir}/icons/*/*/*/*
%{_datadir}/nextcloud
%{_datadir}/mime/packages/nextcloud.xml
%{_datadir}/applications/com.nextcloud.desktopclient.nextcloud.desktop
%{_bindir}/nextcloud
%{_bindir}/nextcloudcmd
%{_sysconfdir}/Nextcloud

%files dolphin
%{_libdir}/libnextclouddolphinpluginhelper.so
%{_libdir}/qt5/plugins/kf5/overlayicon/nextclouddolphinoverlayplugin.so
%{_libdir}/qt5/plugins/kf5/kfileitemaction/nextclouddolphinactionplugin.so

%files nautilus
%{_datadir}/nautilus-python/extensions/*

%files caja
%{_datadir}/caja-python/extensions/*

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n desktop-%{version}
%cmake_kde5 \
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	-DNO_SHIBBOLETH=True \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF

%build
export LD_LIBRARY_PATH=%{_libdir}/nextcloud
%ninja -C build

%install
%ninja_install -C build
