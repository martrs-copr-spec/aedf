%global _gitcommit 588546f0831b7f3d0b7f003724b438f5761befbd
%global _gitdate 20200714

Name:           fuseiso3
Version:        1.3git%{_gitdate}
Release:        2%{?dist}
Summary:        Mount ISO filesystem images as a non-root user

License:        GPLv2
URL:            https://github.com/kuenishi/fuseiso3/
Source0:        https://github.com/kuenishi/fuseiso3/archive/%{_gitcommit}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++ glibc-devel
#BuildRequires:  autoconf automake libtool intltool
BuildRequires:  pkgconfig(fuse) pkgconfig(glib-2.0) pkgconfig(zlib-ng)

%description
Mount ISO filesystem images as a non-root user. Currently supports
plain ISO9660 Level 1 and 2, Rock Ridge, Joliet, zisofs. 
Supported image types: ISO, BIN (single track only), NRG, MDF, IMG (CCD).

fuseiso3 attempts to modernize fuseiso https://sourceforge.net/p/fuseiso/
with patches from https://github.com/KaOS-Community-Packages/fuseiso


%prep
%autosetup -n %{name}-%{_gitcommit}


%build
#autoreconf -fi
%configure
%make_build


%install
%make_install


%files
%license AUTHORS COPYING
%doc ChangeLog INSTALL NEWS README TODO
%{_bindir}/fuseiso


%changelog
* Mon May 12 2025 Martin RS - 1.3git20200714
- Initial for Fedora
