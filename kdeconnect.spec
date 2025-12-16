#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define oname kdeconnect-kde

Summary:	Connect KDE with your smartphone
Name:		kdeconnect
Version:	25.12.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://albertvaka.wordpress.com/
%if 0%{?git:1}
Source0:	https://invent.kde.org/network/kdeconnect-kde/-/archive/%{gitbranch}/kdeconnect-kde-%{gitbranchd}.tar.bz2#/kdeconnect-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{oname}-%{version}.tar.xz
%endif
# (tpg) add firewalld rule
# https://issues.openmandriva.org/show_bug.cgi?id=1491
Source1:	kde-connect.xml
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6People)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6PulseAudioQt)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6QQC2DesktopStyle)
BuildRequires:	cmake(KF6Package)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libfakekey)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	cmake(Qt6Bluetooth)
BuildRequires:	pkgconfig(Qt6Multimedia)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	cmake(Qca-qt6)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	cmake(WaylandProtocols)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	cmake(Qt6WlShellIntegrationPrivate)
BuildRequires:	cmake(KF6ModemManagerQt)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	kirigami-addons
Requires:	kf6-kirigami
Requires:	kirigami-addons
Requires:	%{_lib}Qt6QuickControls2
Requires:	qt6-qtdeclarative
Requires:	sshfs
Requires:	%{_lib}qca-qt6-plugin-openssl
Requires(post):	/bin/sh

%rename plasma6-kdeconnect

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DEXPERIMENTALAPP_ENABLED=ON

%patchlist

%description
KDE Connect is a module to connect KDE with your smartphone.
You need to install KdeConnect.apk on your smartphone to make it work.

%package nautilus
Summary:	KDE Connect integration for Nautilus
Recommends:	nautilus
Requires:	%{name} = %{EVRD}
%rename plasma6-kdeconnect-nautilus

%description nautilus
KDE Connect integration for Nautilus

%package thunar
Summary:	KDE Connect integration for Thunar
Recommends:	thunar
Requires:	%{name} = %{EVRD}
%rename plasma6-kdeconnect-thunar

%description thunar
KDE Connect integration for Thunar

%package deepin
Summary:	KDE Connect integration for the deepin file manager
Requires:	%{name} = %{EVRD}
%rename plasma6-kdeconnect-deepin

%description deepin
KDE Connect integration for the deepin file manager

%files -f %{name}.lang
%{_bindir}/kdeconnect-app
%{_bindir}/kdeconnect-cli
%{_bindir}/kdeconnect-handler
%{_bindir}/kdeconnect-indicator
%{_bindir}/kdeconnect-sms
%{_bindir}/kdeconnectd
%{_libdir}/libkdeconnectcore.so.*
%{_datadir}/applications/*.desktop
%{_datadir}/knotifications6/kdeconnect.notifyrc
%{_sysconfdir}/xdg/autostart/org.kde.kdeconnect.daemon.desktop
%{_datadir}/dbus-1/services/org.kde.kdeconnect.service
%{_qtdir}/plugins/kdeconnect
%{_qtdir}/plugins/kf6/kio/*.so
%{_qtdir}/plugins/kf6/kfileitemaction/*.so
%dir %{_datadir}/plasma/plasmoids/org.kde.kdeconnect/
%{_datadir}/plasma/plasmoids/org.kde.kdeconnect/*
%dir %{_qtdir}/qml/org/kde/kdeconnect
%{_qtdir}/qml/org/kde/kdeconnect/*
%{_prefix}/lib/firewalld/services/kde-connect.xml
%{_datadir}/kdeconnect
%{_datadir}/qlogging-categories6/kdeconnect-kde.categories
%{_datadir}/contractor/kdeconnect.contract
%{_datadir}/icons/*/*/*/*
%{_datadir}/zsh/site-functions/_kdeconnect
%{_datadir}/metainfo/org.kde.kdeconnect.metainfo.xml
%{_sysconfdir}/ufw/applications.d/kdeconnect

%files nautilus -f kdeconnect-nautilus-extension.lang
%{_datadir}/nautilus-python/extensions/kdeconnect-share.py

%files thunar
%{_datadir}/Thunar/sendto/kdeconnect-thunar.desktop

%files deepin
%{_datadir}/deepin/dde-file-manager/oem-menuextensions/kdeconnect-dde.desktop

#----------------------------------------------------------------------------

%install -a
install -m644 -p -D %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/services/kde-connect.xml

# No need to package a static helper lib
rm %{buildroot}%{_libdir}/*.a

%find_lang kdeconnect kdeconnect-cli kdeconnect-core kdeconnect-fileitemaction kdeconnect-kcm kdeconnect-kde kdeconnect-kded kdeconnect-plugins kdeconnect-kio kdeconnect-urlhandler plasma_applet_org.kde.kdeconnect kdeconnect-sms kdeconnect-app kdeconnect-indicator kdeconnect-interfaces kdeconnect-settings %{name}.lang --with-html
%find_lang kdeconnect-nautilus-extension --with-html

%post
# (tpg) reload firewalld
if [ -x /usr/bin/firewall-cmd ]; then
	/usr/bin/firewall-cmd --permanent --add-service kde-connect 2&>1 ||:
	/usr/bin/firewall-cmd --reload 2&>1 ||:
fi
