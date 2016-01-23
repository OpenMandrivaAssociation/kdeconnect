%define oname kdeconnect-kde

Summary:	Connect KDE with your smartphone
Name:		kdeconnect
Version:	0.9
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://albertvaka.wordpress.com/
Source0:	http://download.kde.org/unstable/kdeconnect/%{version}/src/%{oname}-%{version}g.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(libfakekey)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)
Requires:	sshfs

%description
KDE Connect is a module to connect KDE with your smartphone.
You need to install KdeConnect.apk on your smartphone to make it work.

%files -f %{name}.lang
%{_kde5_bindir}/kcapp
%{_kde5_bindir}/kdeconnect-cli
%{_kde5_applicationsdir}/*.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kdeconnect.*
%{_kde5_iconsdir}/hicolor/*/status/laptop-*.*
%{_kde5_iconsdir}/hicolor/*/status/smartphone-*.*
%{_kde5_iconsdir}/hicolor/*/status/tablet-*.*
%{_kde5_libexecdir}/kdeconnectd
%{_kde5_notificationsdir}/kdeconnect.notifyrc
%{_kde5_services}/kcm_kdeconnect.desktop
%{_kde5_services}/kdeconnect_pausemusic_config.desktop
%{_kde5_services}/kdeconnect_share_config.desktop
%{_kde5_services}/kdeconnectsendfile.desktop
%{_kde5_servicetypes}/kdeconnect_plugin.desktop
%{_kde5_autostart}/kdeconnectd.desktop
%{_datadir}/dbus-1/services/org.kde.kdeconnect.service
%{_qt5_plugindir}/kcm_kdeconnect.so
%{_qt5_plugindir}/kdeconnect_pausemusic_config.so
%{_qt5_plugindir}/kdeconnect_share_config.so
%{_qt5_plugindir}/kdeconnectfiletiemaction.so
%{_qt5_plugindir}/kdeconnect/kdeconnect_*.so
%dir %{_kde5_datadir}/plasma/plasmoids/org.kde.kdeconnect/
%{_kde5_datadir}/plasma/plasmoids/org.kde.kdeconnect/*
%{_kde5_services}/plasma-kdeconnect.desktop
%dir %{_kde5_qmldir}/org/kde/kdeconnect
%{_kde5_qmldir}/org/kde/kdeconnect/*
%{_kde5_services}/kdeconnect.protocol
%{_qt5_plugindir}/kio_kdeconnect.so

#----------------------------------------------------------------------------

%define core_major 1
%define libcore %mklibname kdeconnectcore %{core_major}

%package -n %{libcore}
Summary:	Shared library for KDE Connect
Group:		System/Libraries

%description -n %{libcore}
Shared library for KDE Connect.

%files -n %{libcore}
%{_kde_libdir}/libkdeconnectcore.so.%{core_major}*

#----------------------------------------------------------------------------

%define interfaces_major 1
%define libinterfaces %mklibname kdeconnectinterfaces %{interfaces_major}

%package -n %{libinterfaces}
Summary:	Shared library for KDE Connect
Group:		System/Libraries

%description -n %{libinterfaces}
Shared library for KDE Connect.

%files -n %{libinterfaces}
%{_kde_libdir}/libkdeconnectinterfaces.so.%{interfaces_major}*

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}
%cmake_kde5 -DEXPERIMENTALAPP_ENABLED=ON

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kdeconnect-cli kdeconnect-core kdeconnect-fileitemaction kdeconnect-kcm kdeconnect-kded kdeconnect-plugins kdeconnect-kio plasma_applet_org.kde.kdeconnect %{name}.lang
