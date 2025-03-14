# %{_bindir}/nextcloud needs rpath to find its helper
# libraries in %{_libdir}/nextcloud
%global dont_remote_rpath 1

%define libname %mklibname nextcloudsync 2
%define devname %mklibname -d nextcloudsync

Summary:	Client for the NextCloud cloud storage system
Name:		nextcloud-client
Version:	3.16.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://github.com/nextcloud/desktop
Source0:	https://github.com/nextcloud/desktop/archive/v%{version}/desktop-%{version}.tar.gz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	cmake(Qt6WebSockets)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(DolphinVcs) > 23.06.0
BuildRequires:  doxygen
BuildRequires:  inotify-tools
BuildRequires:  inotifytools-devel
#BuildRequires:  pkgconfig(cloudproviders)
BuildRequires:	pkgconfig(libp11)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(xkbcommon-x11)
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

%files -f %{name}.lang
%{_datadir}/nemo-python
%{_datadir}/icons/*/*/*/*
%{_datadir}/mime/packages/nextcloud.xml
%{_datadir}/applications/com.nextcloud.desktopclient.nextcloud.desktop
%{_bindir}/nextcloud
%{_bindir}/nextcloudcmd
%{_sysconfdir}/Nextcloud
%dir %{_datadir}/nextcloud
%dir %{_datadir}/nextcloud/i18n

%files dolphin
%{_libdir}/libnextclouddolphinpluginhelper.so
%{_libdir}/qt6/plugins/kf6/kfileitemaction/nextclouddolphinactionplugin.so
%{_libdir}/qt6/plugins/kf6/overlayicon/nextclouddolphinoverlayplugin.so

%files nautilus
%{_datadir}/nautilus-python/extensions/*

%files caja
%{_datadir}/caja-python/extensions/*

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n desktop-%{version}
%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	-DNO_SHIBBOLETH=True \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
	-G Ninja

%build
export LD_LIBRARY_PATH=%{_libdir}/nextcloud
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-qt
