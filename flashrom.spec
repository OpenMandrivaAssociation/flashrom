%define name flashrom
%define version 0.9.0 
%define release %mkrel 1

Summary: Utility which can be used to detect/read/write BIOS chips 
Name: %{name}
Epoch: 1
Version: %{version}
Release: %{release}
Source0: http://qa.coreboot.org/releases/%{name}-%{version}.tar.gz
License: GPLv2+
Group: System/Kernel and hardware
Url: http://coreboot.org/flashrom
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: pciutils-devel, zlib-devel, glibc-static-devel

%description
Flashrom is a utility which can be used to detect BIOS chips (DIP, PLCC),
read their contents and write new contents on the chips ("flash the chip").

%prep
%setup -q

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

