%define _gitcommit c710d851a9b9c1759ac8597e12f55ea290a3f007
%define _gitdate 20210920

%define srcname sfArkLib

Name:           sfarklib
Version:        2.24git%{_gitdate}
Release:        3%{?dist}
Summary:        Library for decompressing sfArk soundfonts

License:        GPLv3
URL:            https://github.com/raboof/sfArkLib
Source0:        https://github.com/raboof/sfArkLib/archive/%{_gitcommit}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc-c++ glibc-devel
BuildRequires:  pkgconfig(zlib)

%description
Library for decompressing sfArk soundfonts.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(zlib)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{srcname}-%{_gitcommit}
sed -i Makefile \
  -e 's/^\(INSTALL +=\)/override \1/' \
  -e '/INSTALL) [a-zA-Z]*\.h/s/\(INSTALL)\)/\1 -m644/'

%build
%make_build


%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}


%files
%license COPYING
%doc README.md
%{_libdir}/libsfark.so.*

%files devel
%{_includedir}/sfArkLib.h
%{_libdir}/libsfark.so


%changelog
* Fri May 23 2025 Martin RS - 2.24git20210920
- update
* Sun Dec 26 2021 Martin RS - 2.24
- Initial for Fedora
