Summary:	Connect KDE with your smartphone
Name:		kdeconnect
Version:	0.4.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://albertvaka.wordpress.com/
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{name}/%{version}/src/%{name}-kde-%{version}.tar.xz
# Based on 0.3 and l10n svn
Source1:	kdeconnect-kde-i18n.tar.bz2
Patch0:		kdeconnect-kde-0.4.1-cmake-po.patch
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(QJson)

%description
KDE Connect is a module to connect KDE with your smartphone.
You need to install KdeConnect.apk on your smartphone to make it work.

%files -f %{name}.lang
%{_kde_appsdir}/%{name}
%{_kde_appsdir}/plasma/plasmoids/%{name}
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
%{_kde_servicetypes}/kdeconnect_plugin.desktop
%{_datadir}/dbus-1/interfaces/*.xml

#----------------------------------------------------------------------------

%define major 1
%define libname %mklibname %{name} %{major}

%package -n %{libname}
Summary:	Shared library for KDE Connect
Group:		System/Libraries

%description -n %{libname}
Shared library for KDE Connect.

%files -n %{libname}
%{_kde_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-kde-%{version}
%patch0 -p1

tar -xf %{SOURCE1}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_kde_libdir}/lib%{name}.so

%find_lang kdeconnect-kcm kdeconnect-kded kdeconnect-plasmoid %{name}.lang

