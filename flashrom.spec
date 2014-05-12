%define debug_package %{nil}

Summary:	Utility which can be used to detect/read/write BIOS chips 
Name:		flashrom
Epoch:		1
Version:	0.9.7
Release:	1
Source0:	http://download.flashrom.org/releases/%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://flashrom.org
BuildRequires:	pciutils-devel
BuildRequires:	zlib-devel
BuildRequires:	glibc-static-devel

%description
Flashrom is a utility which can be used to detect BIOS chips (DIP, PLCC),
read their contents and write new contents on the chips ("flash the chip").

%prep
%setup -q

%build
%make

%install
mkdir -p %buildroot/%{_sbindir}
%makeinstall PREFIX=%buildroot/usr

%files
%{_sbindir}/flashrom
%{_mandir}/man8/flashrom*
