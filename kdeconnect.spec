%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define oname kdeconnect-kde

Summary:	Connect KDE with your smartphone
Name:		kdeconnect
Version:	22.12.3
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
BuildRequires:	cmake(KF5QQC2DesktopStyle)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	pkgconfig(libfakekey)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(qca2-qt5)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-scanner)
Requires:	sshfs
Requires:	%{_lib}qca2-plugin-openssl
Requires(post):	/bin/sh
# There is no point in separate libpackages for internal libraries.
# They can't be used outside of kdeconnect (no shipped headers or
# *.so files).
# Get rid of them.
Obsoletes:	%{mklibname kdeconnectcore 0}
Obsoletes:	%{mklibname kdeconnectcore 1}
Obsoletes:	%{mklibname kdeconnectcore 20}
Obsoletes:	%{mklibname kdeconnectcore 21}
Obsoletes:	%{mklibname kdeconnectinterfaces 0}
Obsoletes:	%{mklibname kdeconnectinterfaces 1}
Obsoletes:	%{mklibname kdeconnectinterfaces 20}
Obsoletes:	%{mklibname kdeconnectinterfaces 21}
Obsoletes:	%{mklibname kdeconnectpluginkcm 0}
Obsoletes:	%{mklibname kdeconnectpluginkcm 1}
Obsoletes:	%{mklibname kdeconnectpluginkcm 20}
Obsoletes:	%{mklibname kdeconnectpluginkcm 21}

%description
KDE Connect is a module to connect KDE with your smartphone.
You need to install KdeConnect.apk on your smartphone to make it work.

%package nautilus
Summary:	KDE Connect integration for Nautilus
Supplements:	nautilus
Requires:	%{name} = %{EVRD}

%description nautilus
KDE Connect integration for Nautilus

%package thunar
Summary:	KDE Connect integration for Thunar
Supplements:	thunar
Requires:	%{name} = %{EVRD}

%description thunar
KDE Connect integration for Thunar

%package deepin
Summary:	KDE Connect integration for the deepin file manager
Requires:	%{name} = %{EVRD}

%description deepin
KDE Connect integration for the deepin file manager

%files -f %{name}.lang
%{_bindir}/kdeconnect-app
%{_bindir}/kdeconnect-cli
%{_bindir}/kdeconnect-handler
%{_bindir}/kdeconnect-indicator
%{_bindir}/kdeconnect-settings
%{_bindir}/kdeconnect-sms
%{_libdir}/libkdeconnectcore.so.*
%{_libdir}/libkdeconnectinterfaces.so.*
%{_libdir}/libkdeconnectpluginkcm.so.*
%{_datadir}/metainfo/org.kde.kdeconnect.appdata.xml
%{_kde5_applicationsdir}/*.desktop
%{_kde5_libexecdir}/kdeconnectd
%{_datadir}/knotifications5/kdeconnect.notifyrc
%{_sysconfdir}/xdg/autostart/org.kde.kdeconnect.daemon.desktop
%{_datadir}/dbus-1/services/org.kde.kdeconnect.service
%{_qt5_plugindir}/kcm_kdeconnect.so
%{_qt5_plugindir}/kdeconnect
%{_qt5_plugindir}/kf5/kio/*.so
%{_qt5_plugindir}/kf5/kfileitemaction/*.so
%dir %{_kde5_datadir}/plasma/plasmoids/org.kde.kdeconnect/
%{_kde5_datadir}/plasma/plasmoids/org.kde.kdeconnect/*
%dir %{_kde5_qmldir}/org/kde/kdeconnect
%{_kde5_qmldir}/org/kde/kdeconnect/*
%{_prefix}/lib/firewalld/services/kde-connect.xml
%{_datadir}/kdeconnect
%{_datadir}/qlogging-categories5/kdeconnect-kde.categories
%{_datadir}/contractor/kdeconnect.contract
%{_datadir}/icons/*/*/*/*
%{_datadir}/zsh/site-functions/_kdeconnect
%{_datadir}/kservices5/kcm_kdeconnect.desktop
%{_datadir}/kservices5/plasma-kdeconnect.desktop
%{_datadir}/metainfo/org.kde.kdeconnect.metainfo.xml

%files nautilus -f kdeconnect-nautilus-extension.lang
%{_datadir}/nautilus-python/extensions/kdeconnect-share.py

%files thunar
%{_datadir}/Thunar/sendto/kdeconnect-thunar.desktop

%files deepin
%{_datadir}/deepin/dde-file-manager/oem-menuextensions/kdeconnect-dde.desktop

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}
%cmake_kde5 -DEXPERIMENTALAPP_ENABLED=ON

%build
%ninja -C build

%install
%ninja_install -C build

install -m644 -p -D %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/services/kde-connect.xml

%find_lang kdeconnect kdeconnect-cli kdeconnect-core kdeconnect-fileitemaction kdeconnect-kcm kdeconnect-kde kdeconnect-kded kdeconnect-plugins kdeconnect-kio kdeconnect-urlhandler plasma_applet_org.kde.kdeconnect kdeconnect-sms kdeconnect-app kdeconnect-indicator kdeconnect-interfaces kdeconnect-settings %{name}.lang --with-html
%find_lang kdeconnect-nautilus-extension --with-html

%post
# (tpg) reload firewalld
if [ -x /usr/bin/firewall-cmd ]; then
    /usr/bin/firewall-cmd --permanent --add-service kde-connect 2&>1 ||:
    /usr/bin/firewall-cmd --reload 2&>1 ||:
fi
