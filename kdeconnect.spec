Summary:	Connect KDE with your smartphone
Name:		kdeconnect
Version:	0.1
Release:	1
# In fact, unknown but let's keep KDE license
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://albertvaka.wordpress.com/
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{name}/%{version}/src/%{name}-kde-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(QJson)

%description
KDE Connect is a module to connect KDE with your smartphone.
You need to install KdeConnect.apk on your smartphone to make it work.

%files
%{_kde_appsdir}/%{name}
%{_kde_appsdir}/plasma/plasmoids/%{name}
%{_kde_libdir}/kde4/kcm_kdeconnect.so
%{_kde_libdir}/kde4/kded_kdeconnect.so
%{_kde_libdir}/kde4/kdeconnect_clipboard.so
%{_kde_libdir}/kde4/kdeconnect_mpriscontrol.so
%{_kde_libdir}/kde4/kdeconnect_notifications.so
%{_kde_libdir}/kde4/kdeconnect_pausemusic.so
%{_kde_libdir}/kde4/kdeconnect_ping.so
%{_kde_libdir}/kde4/kdeconnect_telephony.so
%{_kde_libdir}/kde4/imports/org/kde/kdeconnect
%{_kde_services}/kcm_kdeconnect.desktop
%{_kde_services}/kded/kdeconnect.desktop
%{_kde_services}/kdeconnect_clipboard.desktop
%{_kde_services}/kdeconnect_mpriscontrol.desktop
%{_kde_services}/kdeconnect_notifications.desktop
%{_kde_services}/kdeconnect_pausemusic.desktop
%{_kde_services}/kdeconnect_ping.desktop
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

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_kde_libdir}/lib%{name}.so

