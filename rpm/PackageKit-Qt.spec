Summary:   Qt support library for PackageKit
Name:      PackageKit-Qt
Version:   0.8.8+nemo1
Release:   1
License:   GPLv2+
Group:     System/Libraries
URL:       http://www.packagekit.org
Source0:   http://www.packagekit.org/releases/%{name}-%{version}.tar.xz

Requires: PackageKit >= 0.8.9
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtDBus)
BuildRequires: pkgconfig(QtSql)
BuildRequires: cmake >= 2.8.7
BuildRequires: PackageKit >= 0.8.9

%description
PackageKit-qt is a Qt support library for PackageKit

%package devel
Summary: Development headers for PackageKit-Qt
License: LGPLv2+
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Development headers and libraries for PackageKit-Qt.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
rm -f CMakeCache.txt && mkdir -p build && cd build
cmake ..
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
cd build
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS
%{_libdir}/*packagekit-qt2.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS
%{_libdir}/libpackagekit-qt*.so
%{_libdir}/pkgconfig/packagekit-qt2.pc
%dir %{_includedir}/PackageKit/packagekit-qt2
%{_includedir}/PackageKit/packagekit-qt2/*
%dir %{_libdir}/cmake/packagekit-qt2
%{_libdir}/cmake/packagekit-qt2/*.cmake
