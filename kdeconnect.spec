%define snapshot 20130806

Summary:	Connect KDE with your smartphone
Name:		kdeconnect
Version:	0
Release:	0.%{snapshot}.1
# In fact, unknown but let's keep KDE license
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://albertvaka.wordpress.com/
# git clone git://anongit.kde.org/scratch/albertvaka/kdeconnect-kded
Source0:	%{name}-%{snapshot}.tar.bz2
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(QJson)

%description
KDE Connect is a module to connect KDE with your smartphone.
You need to install KdeConnect.apk on your smartphone to make it work.

%files
%{_kde_appsdir}/%{name}
%{_kde_libdir}/kde4/kcm_kdeconnect.so
%{_kde_libdir}/kde4/kded_kdeconnect.so
%{_kde_services}/kcm_kdeconnect.desktop
%{_kde_services}/kded/kdeconnect.desktop
%{_datadir}/dbus-1/interfaces/*.xml

#------------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{snapshot}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

