%define name flashrom
%define svnversion 20071017
%define version 0.%{svnversion} 
%define release %mkrel 1

Summary: Utility which can be used to detect/read/write BIOS chips 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{svnversion}.tar.gz
License: GPL
Group: System/Kernel and hardware
Url: http://linuxbios.org/Flashrom
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: pciutils-devel, zlib-devel, glibc-static-devel

%description
Flashrom is a utility which can be used to detect BIOS chips (DIP, PLCC),
read their contents and write new contents on the chips ("flash the chip").

%prep
%setup -q -n %name

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
%makeinstall PREFIX=$RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sbindir}/flashrom
%{_mandir}/man8/flashrom*

