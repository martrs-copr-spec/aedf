%global debug_package %nil

Name:           uif2iso
Version:        0.1.7c
Release:        1%{?dist}
Summary:        Tool to convert single and multipart UIF images to the ISO format

License:        GPLv3
URL:            http://aluigi.org/mytoolz.htm#uif2iso
Source0:        https://github.com/baillow/uif2iso/archive/refs/heads/master.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc glibc-devel openssl-devel zlib-devel

%description
UIF2ISO is an open source command-line/GUI tool for converting single
and multipart UIF images to the original ISO format.
The UIF image (Universal Image Format, although there is nothing of
"universal" in it) in fact is just a compressed CD/DVD image created
through a commercial program called MagicISO.


%prep
%autosetup -n %{name}-master
sed -i Makefile \
  -e 's/^\(prefix\s\+=\).*/\1 \$(PREFIX)/' \
  -e 's/\(\$(BINDIR)\)/\$(DESTDIR)\1/'
#  -e 's/^\(DESTDIR\s\+\)=/\1\?=/'


%build
%make_build PREFIX=%{_prefix}


%install
%make_install PREFIX=%{_prefix}


%files
%license LICENSE
%doc README.md uif2iso.txt
%{_bindir}/%{name}

%changelog
* Sun Jun 28 2020 Martin RS - 0.1.7c
- Initial for Fedora
