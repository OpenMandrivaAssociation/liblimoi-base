%define	major	0
%define	oname	limoi-base
%define	libname	%mklibname %{oname} %{major}
%define	devname	%mklibname -d %{oname}

Summary:	LIM OpenMAX Integration Layer base library
Name:		lib%{oname}
Version:	0.1.4
Release:	1
Group:		System/Libraries
License:	LGPLv2.1+
Url:		https://limoa.sourceforge.net/
Source0:	%{name}-%{version}.tar.xz
Patch0:		liblimoi-base-0.1.4-add-missing-liblimoi-core-linkage.patch

%description
LIM OpenMAX Integration Layer base library.

%libpackage %{oname} %{major}

%package -n	%{devname}
Summary:	Development headers for LIM OpenMAX Integration Layer base library
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
Development headers for LIM OpenMAX Integration Layer base library.

%files -n	%{devname}
%doc COPYING ChangeLog
%dir %{_includedir}/limoi
%{_includedir}/limoi/*.h
%{_libdir}/lib%{oname}.so
%{_libdir}/pkgconfig/lib%{oname}.pc

%prep
%setup -q
%patch0 -p1 -b .linkage~
autoreconf -fiv

%build
%configure2_5x
%make

%install
%makeinstall_std

%changelog
* Wed Apr 9 2014 Per Øyvind Karlsen <proyvind@moondrake.org> 0.1.4-1
- initial release
