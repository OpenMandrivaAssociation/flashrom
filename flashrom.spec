Summary:	Utility which can be used to detect/read/write BIOS chips 
Name:		flashrom
Epoch:		1
Version:	0.9.2
Release:	%mkrel 1
Source0:	http://qa.coreboot.org/releases/%{name}-%{version}.tar.bz2
Source1:	http://qa.coreboot.org/releases/%{name}-%{version}.tar.bz2.asc
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://coreboot.org/flashrom
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pciutils-devel, zlib-devel, glibc-static-devel

%description
Flashrom is a utility which can be used to detect BIOS chips (DIP, PLCC),
read their contents and write new contents on the chips ("flash the chip").

%prep
%setup -q

%build
%make

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

