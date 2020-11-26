%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define oname kdeconnect-kde

Summary:	Connect KDE with your smartphone
Name:		kdeconnect
Version:	20.11.80
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://albertvaka.wordpress.com/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{oname}-%{version}.tar.xz
# (tpg) add firewalld rule
# https://issues.openmandriva.org/show_bug.cgi?id=1491
Source1:	kde-connect.xml
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5People)
BuildRequires:  cmake(KF5PeopleVCard)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(KF5PulseAudioQt)
BuildRequires:	pkgconfig(libfakekey)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(qca2-qt5)
Requires:	sshfs
Requires:	%{_lib}qca2-plugin-openssl
Requires(post):	/bin/sh

%description
KDE Connect is a module to connect KDE with your smartphone.
You need to install KdeConnect.apk on your smartphone to make it work.

%files -f %{name}.lang
%{_bindir}/kdeconnect-app
%{_bindir}/kdeconnect-cli
%{_bindir}/kdeconnect-handler
%{_bindir}/kdeconnect-indicator
%{_bindir}/kdeconnect-settings
%{_bindir}/kdeconnect-sms
%{_libdir}/qt5/plugins/kf5/kfileitemaction/*.so
%{_kde5_applicationsdir}/*.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kdeconnect.*
%{_kde5_iconsdir}/hicolor/*/status/laptop*.*
%{_kde5_iconsdir}/hicolor/*/status/smartphone*.*
%{_kde5_iconsdir}/hicolor/*/status/tablet*.*
%{_kde5_libexecdir}/kdeconnectd
%{_datadir}/knotifications5/kdeconnect.notifyrc
%{_kde5_services}/kcm_kdeconnect.desktop
%{_kde5_services}/kdeconnect_share_config.desktop
%{_kde5_servicetypes}/kdeconnect_plugin.desktop
%{_sysconfdir}/xdg/autostart/org.kde.kdeconnect.daemon.desktop
%{_datadir}/dbus-1/services/org.kde.kdeconnect.service
%{_qt5_plugindir}/kcm_kdeconnect.so
%{_qt5_plugindir}/kdeconnect_share_config.so
%{_qt5_plugindir}/kdeconnect/kdeconnect_*.so
%{_qt5_plugindir}/kdeconnect_runcommand_config.so
%{_qt5_plugindir}/kdeconnect_sendnotifications_config.so
%{_qt5_plugindir}/kdeconnect_findthisdevice_config.so
%{_qt5_plugindir}/kdeconnect_pausemusic_config.so
%dir %{_kde5_datadir}/plasma/plasmoids/org.kde.kdeconnect/
%{_kde5_datadir}/plasma/plasmoids/org.kde.kdeconnect/*
%{_kde5_services}/plasma-kdeconnect.desktop
%{_kde5_services}/kdeconnect_runcommand_config.desktop
%{_kde5_services}/kdeconnect_sendnotifications_config.desktop
%{_kde5_services}/kdeconnect_findthisdevice_config.desktop
%{_kde5_services}/kdeconnect_pausemusic_config.desktop
%dir %{_kde5_qmldir}/org/kde/kdeconnect
%{_kde5_qmldir}/org/kde/kdeconnect/*
%{_qt5_plugindir}//kf5/kio/kdeconnect.so
%{_prefix}/lib/firewalld/services/kde-connect.xml
%{_datadir}/metainfo/org.kde.kdeconnect.kcm.appdata.xml
%{_datadir}/kdeconnect
%{_datadir}/nautilus-python/extensions/kdeconnect-share.py
%{_datadir}/qlogging-categories5/kdeconnect-kde.categories
%lang(en) %{_docdir}/HTML/en/kdeconnect/index.cache.*
%lang(en) %{_docdir}/HTML/en/kdeconnect/index.docbook
%{_datadir}/Thunar/sendto/kdeconnect-thunar.desktop
%{_datadir}/deepin/dde-file-manager/oem-menuextensions/kdeconnect-dde.desktop
%{_datadir}/contractor/kdeconnect.contract
%{_datadir}/icons/*/*/*/*
%{_datadir}/zsh/site-functions/_kdeconnect
%{_datadir}/doc/HTML/*/kdeconnect-kde/index*

#----------------------------------------------------------------------------

%define core_major 20
%define libcore %mklibname kdeconnectcore %{core_major}

%package -n %{libcore}
Summary:	Shared library for KDE Connect
Group:		System/Libraries
Obsoletes:	%{mklibname kdeconnectcore 0} < 1.0
Obsoletes:	%{mklibname kdeconnectcore 1} < 20.0

%description -n %{libcore}
Shared library for KDE Connect.

%files -n %{libcore}
%{_libdir}/libkdeconnectcore.so.%{core_major}*

#----------------------------------------------------------------------------

%define interfaces_major 20
%define libinterfaces %mklibname kdeconnectinterfaces %{interfaces_major}

%package -n %{libinterfaces}
Summary:	Shared library for KDE Connect
Group:		System/Libraries
Obsoletes:	%{mklibname kdeconnectinterfaces 0} < 1.0
Obsoletes:	%{mklibname kdeconnectinterfaces 1} < 20.0

%description -n %{libinterfaces}
Shared library for KDE Connect.

%files -n %{libinterfaces}
%{_libdir}/libkdeconnectinterfaces.so.%{interfaces_major}*

%define plugin_major 20
%define libplugin %mklibname kdeconnectpluginkcm %{plugin_major}

%package -n %{libplugin}
Summary:	Shared library for %{name}
Group:		System/Libraries
Obsoletes:	%{mklibname kdeconnectpluginkcm 0} < 1.0
Obsoletes:	%{mklibname kdeconnectpluginkcm 1} < 20.0

%description -n %{libplugin}
Shared library for %{name}.

%files -n %{libplugin}
%{_kde5_libdir}/libkdeconnectpluginkcm.so.%{plugin_major}*

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}
%cmake_kde5 -DEXPERIMENTALAPP_ENABLED=ON

%build
%ninja -C build

%install
%ninja_install -C build

install -m644 -p -D %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/services/kde-connect.xml

%find_lang kdeconnect kdeconnect-cli kdeconnect-core kdeconnect-fileitemaction kdeconnect-kcm kdeconnect-kded kdeconnect-plugins kdeconnect-kio kdeconnect-urlhandler plasma_applet_org.kde.kdeconnect kdeconnect-nautilus-extension kdeconnect-sms kdeconnect-app kdeconnect-indicator kdeconnect-interfaces kdeconnect-settings %{name}.lang --with-html

%post
# (tpg) reload firewalld
if [ -x /usr/bin/firewall-cmd ]; then
    /usr/bin/firewall-cmd --permanent --add-service kde-connect 2&>1 ||:
    /usr/bin/firewall-cmd --reload 2&>1 ||:
fi
