%global debug_package %nil

Name:           AppleCommander
Version:        1.9.0
Release:        3%{?dist}
Summary:        Tools to manipulate Apple II disk images

License:        GPL-2.0
URL:            https://github.com/AppleCommander/AppleCommander
Source0:        https://github.com/AppleCommander/AppleCommander/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}_java21.patch

BuildRequires:  java-21-openjdk-devel
Requires:       java-21-openjdk

%description
AppleCommander is a cross-platform set of tools used to manipulate Apple
][ disk images. There is a GUI packaged for Windows, Linux, or Mac OS
X, and there are a number of command-line tools that are useful for
build chains.


%prep
%autosetup -p1
sed -i settings.gradle \
  -e '/include.*\(win32\|macos\|linux-arm\|linux-aarch\)/d'
sed -i lib/ac-swt-common/src/test/java/com/webcodepro/applecommander/ui/swt/SwtImageTest.java \
  -e 's/OS_ARCH.equals("arm")/IS_OS_LINUX/'

%build
export PATH=/usr/lib/jvm/java-21-openjdk/bin:${PATH}
./gradlew clean build

%install
mkdir -p %{buildroot}%{_libdir}/%{name} %{buildroot}%{_bindir}
tar -x -C %{buildroot}%{_libdir}/%{name} \
  -f app/gui-swt-linux-x86_64/build/distributions/gui-swt-linux-x86_64-%{version}.tar
mv %{buildroot}%{_libdir}/%{name}/gui-swt-linux-x86_64-%{version}/* \
  %{buildroot}%{_libdir}/%{name}/
rmdir %{buildroot}%{_libdir}/%{name}/gui-swt-linux-x86_64-%{version}
chmod -R a+rX,og-w,u+w %{buildroot}%{_libdir}/%name
rm %{buildroot}%{_libdir}/%{name}/bin/*.bat
ln -s %{_libdir}/%{name}/bin/gui-swt-linux-x86_64 \
  %{buildroot}%{_bindir}/AppleCommander

%files
%license LICENSE
%doc CONTRIB.md DEVELOPER.md README.md TODO VERSIONS
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*


%changelog
* Sat May 10 2025 Martin RS - 1.9.0
- update for java-21
* Fri May  3 2024 Martin RS - 1.9.0
- update 
* Fri Nov  4 2022 Martin RS - 1.8.0
- Initial for Fedora
