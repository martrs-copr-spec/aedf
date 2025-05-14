%global _gitcommit 20bbb576d35292edbd83c94855768d571ca69621
%global _gitdate 20180207

Name:           ecmtools
Version:        1.0git%{_gitdate}
Release:        4%{?dist}
Summary:        ECM encode/decode utilities

License:        GPLv2
URL:            http://www.neillcorlett.com/ecm/
Source0:        https://github.com/kidoz/ecm/archive/%{_gitcommit}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.0_fixint.patch
BuildRequires:  gcc glibc-devel cmake

%description
The ECM format allows you to reduce the size of a typical CD image file
(BIN, CDI, NRG, CCD, or any other format that uses raw sectors; results may
vary).

It works by eliminating the Error Correction/Detection Codes (ECC/EDC) from
each sector whenever possible. The encoder automatically adjusts to
different sector types and automatically skips any headers it encounters.


%prep
%autosetup -p1 -n ecm-%{_gitcommit}
echo -e "\ninstall(TARGETS ecm unecm)" >> CMakeLists.txt


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc doc/format.txt README.md
%{_bindir}/ecm
%{_bindir}/unecm


%changelog
* Sun Jul 5 2020 Martin RS - 1.0git20180207
- Initial for Fedora, fix install
* Wed Jan 15 2014 bb <bb> 1.0-2pclos2014
- fix rpmgroup
* Fri Aug 23 2013 Agent Smith <ruidobranco@yahoo.com.br> 1.0-1pclos2012
- Created package ecmtools
