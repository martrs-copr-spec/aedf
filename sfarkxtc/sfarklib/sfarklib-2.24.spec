Name:           sfarklib
Version:        2.24
Release:        3%{?dist}
Summary:        Library for decompressing sfArk sound fonts

License:        GPLv3
URL:            https://github.com/raboof/sfArkLib
Source0:        https://github.com/raboof/sfArkLib/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         %{name}-%{version}_endian_make.patch

BuildRequires:  gcc-c++ glibc-devel
BuildRequires:  dos2unix
BuildRequires:  pkgconfig(zlib)

%description
%{summary}.

%package	devel
Summary:	%{summary}
Requires:	%{name} = %{version}
Requires:       pkgconfig(zlib)

%description    devel
%{summary}.

%prep
%setup -n sfArkLib-%{version}
chmod a-x *.h *.cpp
dos2unix *.h *.cpp
%patch -P 1 -p1


%build
%make_build


%install
%make_install


%files
%license COPYING
%doc README.md
%{_libdir}/libsfark.so.0

%files devel
%{_includedir}/sfArkLib.h
%{_libdir}/libsfark.so


%changelog
* Sun Dec 26 2021 Martin RS - 2.24
- Initial for Fedora
