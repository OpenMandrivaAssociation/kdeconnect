Summary:	Connect KDE with your smartphone
Name:		kdeconnect
Version:	0.7.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://albertvaka.wordpress.com/
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{name}/%{version}/src/%{name}-kde-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(libfakekey)
BuildRequires:	qca2-devel-qt4

%description
KDE Connect is a module to connect KDE with your smartphone.
You need to install KdeConnect.apk on your smartphone to make it work.

%files -f %{name}.lang
%{_bindir}/kdeconnect-cli
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/%{name}/
%{_kde_appsdir}/plasma/plasmoids/%{name}
%{_kde_iconsdir}/hicolor/*/apps/%{name}.*
%{_kde_libdir}/kde4/kcm_kdeconnect.so
%{_kde_libdir}/kde4/kded_kdeconnect.so
%{_kde_libdir}/kde4/kdeconnect_battery.so
%{_kde_libdir}/kde4/kdeconnect_clipboard.so
%{_kde_libdir}/kde4/kdeconnect_mpriscontrol.so
%{_kde_libdir}/kde4/kdeconnect_notifications.so
%{_kde_libdir}/kde4/kdeconnect_pausemusic.so
%{_kde_libdir}/kde4/kdeconnect_pausemusic_config.so
%{_kde_libdir}/kde4/kdeconnect_ping.so
%{_kde_libdir}/kde4/kdeconnect_share.so
%{_kde_libdir}/kde4/kdeconnect_share_config.so
%{_kde_libdir}/kde4/kdeconnect_telephony.so
%{_kde_libdir}/kde4/imports/org/kde/kdeconnect
%{_kde_libdir}/kde4/libexec/kdeconnectd
%{_kde_libdir}/kde4/kdeconnect_mousepad.so
%{_kde_libdir}/kde4/kdeconnect_sftp.so
%{_kde_libdir}/kde4/kdeconnect_sftp_config.so
%{_kde_libdir}/kde4/kdeconnectfiletiemaction.so
%{_kde_libdir}/kde4/kio_kdeconnect.so
%{_kde_services}/kcm_kdeconnect.desktop
%{_kde_services}/kded/kdeconnect.desktop
%{_kde_services}/kdeconnect_battery.desktop
%{_kde_services}/kdeconnect_clipboard.desktop
%{_kde_services}/kdeconnect_mpriscontrol.desktop
%{_kde_services}/kdeconnect_notifications.desktop
%{_kde_services}/kdeconnect_pausemusic.desktop
%{_kde_services}/kdeconnect_pausemusic_config.desktop
%{_kde_services}/kdeconnect_ping.desktop
%{_kde_services}/kdeconnect_share.desktop
%{_kde_services}/kdeconnect_share_config.desktop
%{_kde_services}/kdeconnect_telephony.desktop
%{_kde_services}/plasma-kdeconnect.desktop
%{_kde_services}/kdeconnect.protocol
%{_kde_services}/kdeconnect_mousepad.desktop
%{_kde_services}/kdeconnect_sftp.desktop
%{_kde_services}/kdeconnect_sftp_config.desktop
%{_kde_services}/kdeconnectsendfile.desktop
%{_kde_servicetypes}/kdeconnect_plugin.desktop
%{_datadir}/dbus-1/interfaces/*.xml

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
%setup -qn %{name}-kde-%{version}

%build
# our qca pkg config is in a non standard path due to qt5/4 split
export PKG_CONFIG_PATH=%{_libdir}/qt4/pkgconfig

%cmake_kde4
%make

%install
%makeinstall_std -C build

# Drop devel files for now because they are messed up
rm -f %{buildroot}%{_kde_libdir}/*.so
rm -rf %{buildroot}%{_kde_libdir}/cmake/
rm -rf %{buildroot}%{_kde_includedir}/

%find_lang kdeconnect-kcm kdeconnect-kded kdeconnect-plasmoid kdeconnect-kio plasma_applet_kdeconnect kdeconnect-plugins kdeconnect-filetiemaction kdeconnect-cli kdeconnect-core %{name}.lang

